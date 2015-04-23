# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen
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
    'scrawlPathFormat': MEDIA_URL + 'ueditor/scrawl/{YYYY}{MM}{DD}/{UUID}',
    'scrawlMaxSize': '2048000',
    'scrawlUrlPrefix': '',
    'scrawlInsertAlign': 'none',
    # 截图工具上传
    'snapscreenActionName': 'uploadimage',
    'snapscreenPathFormat': MEDIA_URL + 'ueditor/snap/{YYYY}{MM}{DD}/{UUID}',
    'snapscreenUrlPrefix': '',
    'snapscreenInsertAlign': 'none',
    # 抓取远程图片配置
    'catcherLocalDomain': ['127.0.0.1', 'localhost', 'img.baidu.com'],
    'catcherActionName': 'catchimage',
    'catcherFieldName': 'source',
    'catcherPathFormat': MEDIA_URL + 'ueditor/cacher/{YYYY}{MM}{DD}/{UUID}',
    'catcherUrlPrefix': '',
    'catcherMaxSize': 2048000,
    'catcherAllowFiles':  ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    # 上传视频配置
    'videoActionName': 'uploadvideo',
    'videoFieldName': 'upfile',
    'videoPathFormat': MEDIA_URL + 'ueditor/video/{YYYY}{MM}{DD}/{UUID}',
    'videoUrlPrefix': '',
    'videoMaxSize': 102400000,
    'videoAllowFiles': [
        '.flv', '.swf', '.mkv', '.avi', '.rm', '.rmvb', '.mpeg', '.mpg',
        '.ogg', '.ogv', '.mov', '.wmv', '.mp4', '.webm', '.mp3', '.wav', '.mid'],
    # 上传文件配置
    'fileActionName': 'uploadfile',
    'fileFieldName': 'upfile',
    'filePathFormat': MEDIA_URL + 'ueditor/file/{YYYY}{MM}{DD}/{UUID}',
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
}