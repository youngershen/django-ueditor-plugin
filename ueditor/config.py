# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    : 
# AUTHOR       : younger shen

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
    'imagePathFormat': '/ueditor/php/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}',
    # 涂鸦图片上传配置项
    'scrawlActionName': 'uploadscrawl',
    'scrawlFieldName': 'upfile',
    'scrawlPathFormat': '/ueditor/php/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}',
    'scrawlMaxSize': '2048000',
    'scrawlUrlPrefix': '',
    'scrawlInsertAlign': 'none',
    # 截图工具上传
    'snapscreenActionName': 'uploadimage',
    'snapscreenPathFormat': '/ueditor/php/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}',
    'snapscreenUrlPrefix': '',
    'snapscreenInsertAlign': 'none',
    # 抓取远程图片配置
    'catcherLocalDomain': ['127.0.0.1', 'localhost', 'img.baidu.com'],
    'catcherActionName': 'catchimage',
    'catcherFieldName': 'source',
    'catcherPathFormat': '/ueditor/php/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}',
    'catcherUrlPrefix': '',
    'catcherMaxSize': 2048000,
    'catcherAllowFiles':  ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    # 上传视频配置
    'videoActionName': 'uploadvideo',
    'videoFieldName': 'upfile',
    'videoPathFormat': '/ueditor/php/upload/video/{yyyy}{mm}{dd}/{time}{rand:6}',
    'videoUrlPrefix': '',
    'videoMaxSize': 102400000,
    'videoAllowFiles': [
        '.flv', '.swf', '.mkv', '.avi', '.rm', '.rmvb', '.mpeg', '.mpg',
        '.ogg', '.ogv', '.mov', '.wmv', '.mp4', '.webm', '.mp3', '.wav', '.mid'],
    # 上传文件配置
    'fileActionName': 'uploadfile',
    'fileFieldName': 'upfile',
    'filePathFormat': '/ueditor/php/upload/file/{yyyy}{mm}{dd}/{time}{rand:6}',
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
    'imageManagerListPath': '/ueditor/php/upload/image/',
    'imageManagerListSize': 20,
    'imageManagerUrlPrefix': '',
    'imageManagerInsertAlign': 'none',
    'imageManagerAllowFiles': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
}