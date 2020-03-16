# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from setuptools import setup, find_packages


packages = find_packages('typeidea')
print(packages)

setup(
    name='utf8',
    version='0.1',
    description='Blog System base on Django',
    author='libsh',
    author_email='l5623064@163.com',
    # url='https://www.the5fire.com',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,  # 方法二  ，配置MANIFEST.in文件
    install_requires=[
        'django==1.11.3',
        'django-autocomplete-light==3.2.10',
        'hiredis==1.0.1'
        'redis==2.10.6',
        'django-ckeditor==5.3.1',
        'django-debug-toolbar==1.11',
        'mysqlclient==1.4.6',
        'Pillow==4.3.0',
        'djangorestframework==3.7.0',
        'django-reversion==2.0.10',
        'Markdown==2.6.9',
        'django-redis==4.8.0',
        'django-import-export==0.5.1',
        'requests==2.23.0',
        'six==1.14.0',
        'gunicorn==19.7.1'
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)