#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Pookz'
SITENAME = u'Words Of Dreammis'
SITEURL = ''

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
         ('You can modify those links in your config file111', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = [u"pelican-plugins"]
PLUGINS = ['sitemap', 'related_posts']  # , 'gzip_cache']

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

# Themes Start
THEME = 'voidy-bootstrap'
SITETAG = "One Man who is insane!!"	    #浏览器tag名称 
SITESUBTITLE =u'一个时常自娱自乐的俗人.' # 副主题
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)
SIDEBAR = "sidebar.html"

SOCIAL = (('Google+', 'http://plus.google.com/107598365859176363115',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/dreammis',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/dreammis',
         'fa fa-github-square fa-fw fa-lg'),
        )

SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", "sb_taglist.html", )

# Themes End


DISQUS_SITENAME = 'bee firedirx'
GOOGLE_ANALYTICS = 'UA-89126305-2'

#KEYWORDS = u"Python, Web, 开源, Django, 杭州, 房地产"






