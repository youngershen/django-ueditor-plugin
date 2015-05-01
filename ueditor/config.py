# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.utils.translation import ugettext as _
from django.conf import settings
MEDIA_URL = settings.MEDIA_URL

CONFIG = {
    # 上传图片配置项
    'imageActionName': 'uploadimage',
    'imageFieldName': 'upfile',
    'imageMaxSize': '2048000',
    'imageAllowFiles': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'imageCompressEnable': True,
    'imageCompressBorder': 1600,
    'imageInsertAlign': 'none',
    'imageUrlPrefix': '',
    'imagePathFormat': MEDIA_URL + 'ueditor/image/{YYYY}{MM}{DD}/',
    # 涂鸦图片上传配置项
    'scrawlActionName': 'uploadscrawl',
    'scrawlFieldName': 'upfile',
    'scrawlPathFormat': MEDIA_URL + 'ueditor/scrawl/{YYYY}{MM}{DD}/',
    'scrawlMaxSize': '2048000',
    'scrawlUrlPrefix': '',
    'scrawlInsertAlign': 'none',
    'scrawlAllowFiles': ['.png'],
    # 截图工具上传
    'snapscreenActionName': 'uploadimage',
    'snapscreenPathFormat': MEDIA_URL + 'ueditor/snap/{YYYY}{MM}{DD}/',
    'snapscreenUrlPrefix': '',
    'snapscreenInsertAlign': 'none',
    # 抓取远程图片配置
    'catcherLocalDomain': ['127.0.0.1', 'localhost', 'img.baidu.com'],
    'catcherActionName': 'catchimage',
    'catcherFieldName': 'source',
    'catcherPathFormat': MEDIA_URL + 'ueditor/cacher/{YYYY}{MM}{DD}/',
    'catcherUrlPrefix': '',
    'catcherMaxSize': 2048000,
    'catcherAllowFiles':  ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    # 上传视频配置
    'videoActionName': 'uploadvideo',
    'videoFieldName': 'upfile',
    'videoPathFormat': MEDIA_URL + 'ueditor/video/{YYYY}{MM}{DD}/',
    'videoUrlPrefix': '',
    'videoMaxSize': 102400000,
    'videoAllowFiles': [
        '.flv', '.swf', '.mkv', '.avi', '.rm', '.rmvb', '.mpeg', '.mpg',
        '.ogg', '.ogv', '.mov', '.wmv', '.mp4', '.webm', '.mp3', '.wav', '.mid'],
    # 上传文件配置
    'fileActionName': 'uploadfile',
    'fileFieldName': 'upfile',
    'filePathFormat': MEDIA_URL + 'ueditor/file/{YYYY}{MM}{DD}/',
    'fileUrlPrefix': '',
    'fileMaxSize': 51200000,
    'fileAllowFiles': [
        '.png', '.jpg', '.jpeg', '.gif', '.bmp',
        '.flv', '.swf', '.mkv', '.avi', '.rm', '.rmvb', '.mpeg', '.mpg',
        '.ogg', '.ogv', '.mov', '.wmv', '.mp4', '.webm', '.mp3', '.wav', '.mid',
        '.rar', '.zip', '.tar', '.gz', '.7z', '.bz2', '.cab', '.iso',
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.md', '.xml'
    ],
    # 列出指定目录下的图片
    'imageManagerActionName': 'listimage',
    'imageManagerListPath': MEDIA_URL,
    'imageManagerListSize': 20,
    'imageManagerUrlPrefix': '',
    'imageManagerInsertAlign': 'none',
    'imageManagerAllowFiles': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    # 列出制定目录下的文件
    'fileManagerActionName': 'listfile',
    'fileManagerListPath': '/ueditor/php/upload/file/',
    'fileManagerUrlPrefix': '',
    'fileManagerListSize': 20,
    'fileManagerAllowFiles': [
        '.png', '.jpg', '.jpeg', '.gif', '.bmp',
        '.flv', '.swf', '.mkv', '.avi', '.rm', '.rmvb', '.mpeg', '.mpg',
        '.ogg', '.ogv', '.mov', '.wmv', '.mp4', '.webm', '.mp3', '.wav', '.mid',
        '.rar', '.zip', '.tar', '.gz', '.7z', '.bz2', '.cab', '.iso',
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.md', '.xml'
    ]
}

# error message
ERRORS = {
    'ERROR_TMP_FILE': _(u'临时文件错误'),
    'ERROR_TMP_FILE_NOT_FOUND': _(u'找不到临时文件'),
    'ERROR_SIZE_EXCEED': _(u'文件大小超出网站限制'),
    'ERROR_TYPE_NOT_ALLOWED': _(u'文件类型不允许'),
    'ERROR_CREATE_DIR': _(u'目录创建失败'),
    'ERROR_DIR_NOT_WRITEABLE': _(u'目录没有写权限'),
    'ERROR_FILE_MOVE': _(u'文件保存时出错'),
    'ERROR_FILE_NOT_FOUND': _(u'找不到上传文件'),
    'ERROR_WRITE_CONTENT': _(u'写入文件内容错误'),
    'ERROR_UNKNOWN': _(u'未知错误'),
    'ERROR_DEAD_LINK': _(u'链接不可用'),
    'ERROR_HTTP_LINK': _(u'链接不是http链接'),
    'ERROR_HTTP_CONTENTTYPE': _(u'链接contentType不正确'),
    'ERROR_FILE_NOT_COMPLETED': _(u'文件未被完整上传'),
    'ERROR_NO_FILE_UPLOAD': _(u'没有文件被上传'),
    'ERROR_EMPTY_FILE': _(u'上传文件为空'),
    'UPLOAD_SUCCESS': 'SUCCESS',
}

CONFIG.update(ERRORS)