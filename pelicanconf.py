#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Farzal Space'
SITEURL = 'https://farzal.space'
DOMAIN = 'farzal.space'

SITE_AUTHOR = 'Farzal'
BIO_TEXT = 'engineer and linux user'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican.</a>'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# SIDEBAR_LINKS = [ '<a href="/archive/">Baca Blog</a>', ]

ICONS_PATH = 'images/icons'

SOCIAL_ICONS = [
    ('mailto:farzalanan.ini@gmail.com', 'Email (farzalanan.ini@gmail.com)', 'fa-envelope'),
    ('http://twitter.com/farzal182', 'Twitter', 'fa-twitter'),
    ('http://instagram.com/farzal182', 'Instagram', 'fa-instagram'),
]

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'neighbors', 'render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]

THEME = 'pneumatic'
THEME_COLOR = '#FF8000'
GOOGLE_FONTS = 'Oxygen'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'linenums': None},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

RELATIVE_URLS = True
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DIRECT_TEMPLATES = [
    'index',
    'archives'
]
CATEGORY_SAVE_AS = ''

TYPOGRIFY = True

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = [
    'images',
    'files',
    'extra'
]

IGNORE_FILES = [
    '.DS_Store',
    'pneumatic.scss',
    'pygments.css'
]

extras = [
    'favicon.ico',
    'robots.txt'
]

EXTRA_PATH_METADATA = {
    'extra/%s' % file: {'path': file} for file in extras
}

GOOGLE_ANALYTICS = 'UA-148195511-2'
DISQUS_SITENAME = 'farzal-space'