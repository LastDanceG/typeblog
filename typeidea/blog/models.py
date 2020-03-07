# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import F


class Post(models.Model):

    STATUS_ITEMS = (
        (1, "上线"),
        (2, "草稿"),
        (3, "删除")
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    category = models.ForeignKey('Category', verbose_name="分类")
    tags = models.ManyToManyField('Tag', verbose_name="标签")

    content = models.TextField(verbose_name="内容", help_text="注：目前仅支持MarkDown格式数据")
    is_markdown = models.BooleanField(verbose_name="使用Markdown格式", default=False)
    html = models.TextField(verbose_name="渲染后样式", default='')
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者")
    pv = models.PositiveIntegerField(default=0, verbose_name="pv")
    uv = models.PositiveIntegerField(default=0, verbose_name="uv")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def increase_pv(self):
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.html = markdown.markdown(self.content, extensions=["codehilite"], extension_configs=config)
        else:
            self.html = self.content

        return super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']


class Category(models.Model):

    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")

    owner = models.ForeignKey(User, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "分类"


class Tag(models.Model):

    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")

    owner = models.ForeignKey(User, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "标签"
