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
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)