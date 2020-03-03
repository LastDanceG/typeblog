# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from typeidea.custom_admin import BaseOwnerAdmin
from typeidea.settings.custom_site import custom_site
from .models import Link, SideBar

# Register your models here.


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href', 'status', 'weight', 'create_time']
    search_fields = ['title', 'status', 'weight']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'
    list_editable = ['status']


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'status', 'display_type', 'create_time']
    search_fields = ['title', 'status']
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'create_time'
    list_editable = ['display_type']
