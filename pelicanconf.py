#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sergey Khatsola'
SITENAME = 'Fzona'
SITEURL = 'https://sysadmin.fzona.com.ua'
PATH = 'content'
TIMEZONE = 'Europe/Kiev'
DEFAULT_LANG = 'ru'

THEME = 'themes/blue'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Добавить линк на соц сеть 1', '#'),
          ('Добавить линк на соц сеть 2', '#'),
          ('Добавить линк на соц сеть 3', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True