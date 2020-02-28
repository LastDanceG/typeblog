# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase

# Create your tests here.
from django.test.utils import override_settings

from blog.models import Category


class TestCategory(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        user = User.objects.create_user('lbs', 'l5612345@163.com', 'password')
        # for i in range(10):
        #     category_name = 'cate_%s' % i
        #     Category.objects.create(name=category_name, owner=user)

        Category.objects.bulk_create([Category(name='cate_blk_%s' % i, owner=user) for i in range(10)])
        pprint(connection.queries)

    @override_settings(DEBUG=True)
    def test_filter(self):
        # categories = Category.objects.all()
        # print categories.query
        categories = Category.objects.all()
        print categories
        # print categories.query
        # print '-----'
        print connection.queries
        # print '-----'
        # print len(categories)
