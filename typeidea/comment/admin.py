# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from typeidea.settings.custom_site import custom_site
from .models import Comment

# Register your models here.


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'nickname', 'status', 'website', 'email', 'create_time']
    search_fields = ['nickname', 'status']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'
