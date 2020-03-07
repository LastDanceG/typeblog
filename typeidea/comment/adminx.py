# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from django.contrib import admin

# from typeidea.custom_site import custom_site
from typeidea.custom_admin import BaseOwnerAdmin
from .models import Comment

# Register your models here.


class CommentAdmin(object):
    list_display = ['target', 'nickname', 'status', 'website', 'email', 'create_time']
    search_fields = ['nickname', 'status']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'

xadmin.site.register(Comment, CommentAdmin)