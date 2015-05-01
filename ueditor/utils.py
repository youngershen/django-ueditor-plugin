# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen
import uuid
import time
import os
import base64 as base64tool
from django.conf import settings
from .config import CONFIG
from .config import ERRORS
from .models import UeditorFile


def get_config():
    local_config = getattr(settings, 'UEDITOR_CONFIG', None)
    if local_config:
        CONFIG.update(**local_config)
    return CONFIG


def get_error_message(code):
    return ERRORS.get(code, '')


def upload_file(request, config, base64=None):
    path = config.get('pathFormat')
    fname = config.get('fieldName')
    size = config.get('maxSize')
    allows = config.get('allowFiles')
    state = None

    upfile = request.FILES.get(fname)

    if base64:
        base64data = request.POST.get(fname)
        upfile = base64tool.decodestring(base64data)
        return save_base64(upfile, path, config.get('oriName'), size, allows)

    if upfile.size > size:
        state = get_error_message('ERROR_SIZE_EXCEED')

    ext = '.' + upfile.name.split('.')[-1]
    if ext not in allows:
        state = get_error_message('ERROR_TYPE_NOT_ALLOWED')

    date = time.gmtime()
    uuid_str = str(uuid.uuid4())
    url = path.format(YYYY=date.tm_year, MM=date.tm_mon, DD=date.tm_mday) + uuid_str + ext
    path = settings.BASE_DIR + path.format(YYYY=date.tm_year, MM=date.tm_mon, DD=date.tm_mday)

    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except IOError:
            state = get_error_message('ERROR_CREATE_DIR')

    filename = path + uuid_str + ext
    with open(filename, 'wb+') as dest:
        for chunk in upfile.chunks():
            try:
                dest.write(chunk)
            except IOError:
                state = get_error_message('ERROR_DIR_NOT_WRITEABLE')
                break
    if state:
        UeditorFile.objects.create(name=uuid_str+ext, type=ext, url=url, status=UeditorFile.UPLOAD_FAILED)
    else:
        UeditorFile.objects.create(name=uuid_str+ext, type=ext, url=url, status=UeditorFile.UPLOAD_SUCCEED)

    ret = {'state': state if state else 'SUCCESS',
           'url': url,
           'title': uuid_str + ext,
           'original': 'original',
           'type': ext,
           'size': size
           }

    return ret


def save_base64(upfile, path, name, size, allows):
    fsize = len(upfile)
    state = None
    if fsize > size:
        state = get_error_message('ERROR_SIZE_EXCEED')

    ext = '.' + name.split('.')[-1]
    if ext not in allows:
        state = get_error_message('ERROR_TYPE_NOT_ALLOWED')

    date = time.gmtime()
    uuid_str = str(uuid.uuid4())
    url = path.format(YYYY=date.tm_year, MM=date.tm_mon, DD=date.tm_mday) + uuid_str + ext
    path = settings.BASE_DIR + path.format(YYYY=date.tm_year, MM=date.tm_mon, DD=date.tm_mday)

    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except IOError:
            state = get_error_message('ERROR_CREATE_DIR')

    filename = path + uuid_str + ext
    with open(filename, 'wb+') as dest:
        try:
            dest.write(upfile)
        except IOError:
            state = get_error_message('ERROR_DIR_NOT_WRITEABLE')
        else:
            dest.flush()

    ret = {'state': state if state else 'SUCCESS',
           'url': url,
           'title': uuid_str + ext,
           'original': 'original',
           'type': ext,
           'size': size
           }

    return ret