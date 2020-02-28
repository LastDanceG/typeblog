# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from blog.models import Post


class Comment(models.Model):

    post = models.ForeignKey(Post, verbose_name="文章")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.nickname

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = verbose_name_plural = "评论"
