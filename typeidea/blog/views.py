# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from blog.models import Post, Tag, Category
from comment.models import Comment
from comment.views import CommentShowMixin
from config.models import SideBar


class CommonMixin(object):

    def get_category_context(self):
        categories = Category.objects.filter(status=1)

        nov_cate = []
        cate = []

        for category in categories:
            if category.is_nav:
                nov_cate.append(category)
            else:
                cate.append(category)
        return {
            'nav_cate': nov_cate,
            'cate': cate,
        }
    
    def get_context_data(self, **kwargs):

        recently_posts = Post.objects.filter(status=1)[:10]
        recently_comment = Comment.objects.filter(status=1)[:3]
        host_posts = Post.objects.filter(status=1).order_by('-pv')[0:10]
        side_bar = SideBar.objects.filter(status=1)

        kwargs.update({
            'recently_posts': recently_posts,
            'recently_comment': recently_comment,
            'side_bar': side_bar,
            'host_posts': host_posts,
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)
        

class BasePostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostsView):

    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if query:
            qs = qs.filter(title__icontains=query)  # "select * from post where title ilike '%{}%'".format(query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        category = qs.filter(category_id=cate_id)
        return category


class TagView(BasePostsView):

    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.post_set.all()
        return queryset


class AuthorView(BasePostsView):

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')

        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(owner_id=author_id)
        return qs


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):

        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):

        session_id = self.request.COOKIES.get('sessionid')
        if not session_id:
            return

        # 增加pv 判断用户是否在60s内访问过
        pv_key = 'pv:{}:{}'.format(session_id, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 60)

        # 增加uv，判断用户是否在24小时内访问过
        uv_key = 'uv:{}:{}'.format(session_id, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60 * 60 * 24)


# ------------------------------以下为FUNCTION VIEW，已弃用-------------------------------------
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
