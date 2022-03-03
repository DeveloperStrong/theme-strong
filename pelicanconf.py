import os
from pydoc import pager
from jinja2 import environmentfilter, environment
import markdown as md

AUTHOR = 'developerstrong'
SITENAME = 'strongtheme'
SITEURL = 'theme-present'
TITLE = 'Theme Strong'

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'es'

DEFAULT_THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)),'themes', 'theme-present')

THEME = 'themes/theme-present'#DEFAULT_THEME                                         

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

READERS={"html": None}

CACHE_CONTENT = False

THEME_STATIC_DIR = 'themes/theme-present'

THEME_STATIC_PATHS = ['static',]

DISPLAY_PAGES_ON_MENU = True

# Controla los templates que se renderizan y terminan en el directorio output
DIRECT_TEMPLATES = ['index','page']

ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
PAGE_SAVE_AS ='pages/{slug}.html'

#PLUGIN_PATHS = ['plugins']
#PLUGINS = ['simple']

''' Variable en donde se establece la cantidad de posibles valores a renderizar dentro de una page de productos '''
GRID_NUMBER = 80