# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    :
# AUTHOR       : younger shen

from setuptools import setup, find_packages

version = '0.1'

setup(name='django-ueditor-plugin',
      version=version,
      description="a backend plugin for ueditor",
      long_description="""\
      a backend plugin for baidu ueditor.

      """,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   ],
      keywords='django-ueditor-plugin, django, ueditor',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='https://github.com/youngershen/django-ueditor-plugin',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'Django >= 1.6',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
