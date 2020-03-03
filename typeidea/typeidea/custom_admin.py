# -*- coding: utf-8 -*-

from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """针对有owner属性的数据，重写
    1、save_model - 保证每条数据都属于当前登录的用户
    2、重写get_queryset - 保证每个用户只能看见自己的文章
    """

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)