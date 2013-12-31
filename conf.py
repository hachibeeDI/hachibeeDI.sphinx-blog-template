# -*- coding: utf-8 -*-

'''
via:
    http://kyon-mm.bitbucket.org/blog/html/2013/05/20/start_tinkerer_on_bitbucket.html
    http://blog.shomah4a.net/2013/02/26/setup_tinkerer.html
    http://d.hatena.ne.jp/rudi/20120106/1325861293
'''

import tinkerer
import tinkerer.paths


def setup(app):
    app.add_config_value(name='gravater_id', default='nongravater', rebuild='html')

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

language = 'en'

# Change this to the name of your blog
project = u'Sushi Ninja'

# Change this to the tagline of your blog
tagline = u'That is all you need to eat'

# Change this to the description of your blog
description = 'I am a beginning learner of English, So I apologize for any confusion.'

# Change this to your name
author = 'OGURA Daiki'
mail_address = '8hachibee125@gmail.com'
import md5
gravater_id = str(md5.new(mail_address).hexdigest())

# Change this to your copyright string
copyright = '2013, ' + author

# Change this to your blog root URL (required for RSS feed)
website = 'http://hachibeeDI.github.io/'

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = None

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'tinkerer.ico'

# Pick another Tinkerer theme or use your own
# html_theme = "boilerplate"
html_theme = "mystyle"

# Theme-specific options, see docs
html_theme_options = {}

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Generate full posts for RSS feed even when using "read more"
rss_generate_full_posts = False

# Number of blog posts per page
posts_per_page = 10

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus']

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['_themes/mystyle/', '_themes', tinkerer.paths.themes]

# Add file patterns to exclude from build
exclude_patterns = ["_templates/*", "drafts/*", ]

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": ["searchbox.html", "author.html", "recent.html", "categories.html", "tags.html", ]
}

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
