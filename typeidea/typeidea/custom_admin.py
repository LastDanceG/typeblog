# -*- coding: utf-8 -*-
import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin(object):
    """针对有owner属性的数据，重写
    1、save_model - 保证每条数据都属于当前登录的用户
    2、重写get_queryset - 保证每个用户只能看见自己的文章
    """

    def save_models(self):
        if not self.org_obj:
            self.new_obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_models()

    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


class GlobalSetting(CommAdminView):

    site_title = 'UTF-8'
    site_footer = 'power by libsh'

xadmin.site.register(CommAdminView, GlobalSetting)