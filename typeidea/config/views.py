# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views.generic import ListView

from blog.views import CommonMixin
from comment.views import CommentShowMixin
from config.models import Link


class LinkView(CommonMixin, CommentShowMixin, ListView):

    queryset = Link.objects.filter(status=1)
    template_name = 'config/links.html'
    context_object_name = 'links'
