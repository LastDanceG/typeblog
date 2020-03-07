# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from blog.models import Post


class Comment(models.Model):

    STATUS_ITEMS = (
        (1, "正常"),
        (2, "删除"),
    )

    target = models.CharField(max_length=50, null=True, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
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
        ordering = ['-id']
