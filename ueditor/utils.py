# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.conf import settings
from .config import CONFIG


def get_config():
    local_config = getattr(settings, 'UEDITOR_CONFIG', None)
    if local_config:
        CONFIG.update(**local_config)
    return CONFIG