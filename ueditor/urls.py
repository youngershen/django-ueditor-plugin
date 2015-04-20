# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('ueditor.views', url(r'controller/$', 'controller_view', name='controller_view'),)