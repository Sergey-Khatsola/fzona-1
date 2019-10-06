#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sergey Khatsola'
SITENAME = 'Fzona'
SITEURL = 'https://sysadmin.fzona.com.ua'
PATH = 'content'
TIMEZONE = 'Europe/Kiev'
DEFAULT_LANG = 'ru'

THEME = 'themes/pelican-blue-idea'
# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU (True)

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU (True)

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU (False)

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO (False)

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO (False)

# Display the search form
DISPLAY_SEARCH_FORM (False)

# Sort pages list by a given attribute
PAGES_SORT_ATTRIBUTE (Title)

# Display the "Fork me on Github" banner
GITHUB_URL (None)

# Blogroll
LINKS 

# Social widget
SOCIAL

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