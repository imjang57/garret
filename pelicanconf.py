#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

################################################################################
# Site information
AUTHOR = 'imjang57'
SITENAME = 'garret'
SITEURL = ''

################################################################################
# Paths
PATH = 'content'
# Relative to PATH
OUTPUT_PATH = 'output/'
# Relative to PATH
PAGE_PATHS = ['pages']
# Relative to PATH
STATIC_PATHS = ['images']

################################################################################
# Site generation options
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
# title => slugify from Title: metadata
# basename => slugify from file name
SLUGIFY_SOURCE = 'title'
ARTICLE_EXCLUDES = ['templates']

################################################################################
TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
