# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from typeidea.custom_admin import BaseOwnerAdmin
from typeidea.settings.custom_site import custom_site
from .models import Post, Category, Tag
# Register your models here.


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):

    list_display = [
        'title', 'category', 'status',
        'create_time', 'update_time', 'operator'
    ]
    search_fields = ['owner__username', 'category__name', 'title']
    list_filter = ['owner', 'status']
    save_on_top = True
    show_full_result_count = False
    # list_display_links = ['category', 'title']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'
    list_editable = ['status']

    # 编辑界面
    # 和fields互斥
    fieldsets = (
        ('基础配置', {
            'fields': (('title',), ('category', 'status'), 'desc', 'content')
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),
            'fields': ('tags',)
        })
    )

    filter_horizontal = ('tags',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = "操作"


class PostInline(admin.TabularInline):   # TabularInline 为横向展示。 StackedInline 为竖向展示
    fields = ('title', 'desc', 'status')
    extra = 1  # 默认为4个，即最多展示4篇文章
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]
    list_display = ['name', 'status', 'is_nav', 'create_time']
    search_fields = ['name']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'
    list_editable = ['status']


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'create_time']
    search_fields = ['name']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'
    list_editable = ['status']



