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
LINKS = (('Github', 'https://github.com/imjang57'),
         ('Github site repo', 'https://github.com/imjang57/garret'),
         ('Site', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/imjang57'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

################################################################################
# Google Analytics
GOOGLE_ANALYTICS = 'UA-90095241-1'
