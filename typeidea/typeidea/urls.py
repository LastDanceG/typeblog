# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

import xadmin
from xadmin.plugins import xversion
from ckeditor_uploader import urls as uploader_urls

from typeidea.autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.views import IndexView, TagView, CategoryView, PostView, AuthorView
from comment.views import CommentView
from config.views import LinkView
from typeidea.custom_admin import BaseOwnerAdmin  # NOQA
xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'post/(?P<pk>\d+)/$', PostView.as_view(), name='detail'),
    url(r'author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkView.as_view(), name='link'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^admin/', xadmin.site.urls),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete')
] + uploader_urls.urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
