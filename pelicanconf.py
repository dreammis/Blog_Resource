#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Pookz'
SITENAME = u'Words Of Dreammis'
SITEURL = 'blog.pookz.me'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'Chinese (Simplified)'

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

PLUGIN_PATHS = [u"pelican-plugins"]
PLUGINS = ['sitemap']  # , 'gzip_cache']

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Themes
THEME = 'voidy-bootstrap'
DISQUS_SITENAME = 'bee firedirx'
GOOGLE_ANALYTICS = 'UA-89126305-2'

#KEYWORDS = u"Python, Web, 开源, Django, 杭州, 房地产"

SITESUBTITLE =u'一个时常自娱自乐的俗人.'
SITETAG = "One Man who is insane!!"

