# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen
import uuid
import time
import os
from django.conf import settings
from .config import CONFIG


def get_config():
    local_config = getattr(settings, 'UEDITOR_CONFIG', None)
    if local_config:
        CONFIG.update(**local_config)
    return CONFIG


def upload_file(request, config):
    path = config.get('pathFormat')
    fname = config.get('fieldName')
    size = config.get('maxSize')
    allows = config.get('allowFiles')

    upfile = request.FILES.get(fname)
    print dir(upfile)
    # sie
    if upfile.size > size:
        return dict(name='size is too big')

    # type
    ext = '.' + upfile.name.split('.')[-1]
    if ext not in allows:
        return dict(name='not allowed')

    date = time.gmtime()
    uuid_str = str(uuid.uuid4())
    url = path.format(YYYY=date.tm_year, MM=date.tm_mon, DD=date.tm_mday) + uuid_str + ext
    path = settings.BASE_DIR + path.format(YYYY=date.tm_year, MM=date.tm_mon, DD=date.tm_mday)

    if not os.path.isdir(path):
        os.makedirs(path)

    filename = path + uuid_str + ext
    with open(filename, 'wb+') as dest:
        for chunk in upfile.chunks():
            dest.write(chunk)

    return dict(name=url)


