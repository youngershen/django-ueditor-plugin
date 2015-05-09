#django-ueditor-plugin
------------
__what?__

the plugin is a [ueditor](http://ueditor.baidu.com/website/) django backend ware, just add it to your django project, then you can use ueditor  full featured, the official backend is just for demo usage so i create this ware to my own productive usage.

__how?__

pip install [django-ueditor-plugin](https://github.com/youngershen/django-ueditor-plugin) or add the ware in your requirements.txt ,  then add the plugin to your settings.py

    INSTALLED_APPS = (
    ...
    'ueditor',
    ...
    )
    
and urls.py

        urlpatterns += url(r'^ueditor/', include('ueditor.urls')),


then you should migrate the database

    for south : python manage.py migrate ueditor
    for django 1.7+ : python manage.py migrate ueditor
    or python manage.py syncdb --all


at last, you should use /ueditor/controller/ to your ueditor server url.


__at last__

you can do everything about my bad work, i know no one use it except myself.