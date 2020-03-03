# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from blog.models import Post, Tag, Category
from comment.models import Comment
from config.models import SideBar


def get_common_context():
    categories = Category.objects.all()

    nav_cate = []
    cate = []
    for category in categories:
        if category.is_nav:
            nav_cate.append(category)
        else:
            cate.append(category)

    side_bar = SideBar.objects.filter(status=1)
    recently_posts = Post.objects.filter(status=1)[0:10]
    # host_posts = Post.objects.filter(status=1).order_by('views')[0:10]
    recently_comment = Comment.objects.filter(status=1)[:10]

    context = {
        'nav_cate': nav_cate,
        'cate': cate,
        'side_bar': side_bar,
        'recently_posts': recently_posts,
        'recently_comment': recently_comment,
    }
    return context


def post_list(request, category_id=None, tag_id=None):

    queryset = Post.objects.all()
    page = request.GET.get('page', 1)
    page_size = 1
    try:
        page = int(page)
    except TypeError:
        page = 1

    if category_id:
        # 分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        # 标签页面
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.post_set.all()

        # queryset = queryset.filter(tag_id=tag_id)

    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    common_context = get_common_context()
    context.update(common_context)

    return render(request, template_name='blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('post does not exist')

    context = {
        'post': post,
    }
    common_context = get_common_context()
    context.update(common_context)

    return render(request, template_name='blog/detail.html', context=context)
