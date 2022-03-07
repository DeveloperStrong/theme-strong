import os

AUTHOR = 'developerstrong'
SITENAME = 'strongtheme'
SITEURL = 'https://www.theme-present.com/a/p'
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
DIRECT_TEMPLATES = ['index','page','category','categories']

ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = 'cat/{slug}.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = ''
PAGE_SAVE_AS = '{slug}.html'



# Como son guardadas las urls dentro del output  
PAGE_URL = '{slug}.html'
CATEGORY_URL = 'cat/{slug}'
CATEGORIES_URL = 'categories'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

''' Variable en donde se establece la cantidad de posibles valores a renderizar dentro de una page de productos '''
GRID_NUMBER = 80

SITEMAP = {
    "exclude":['{slug}.html', 'cat/{slug}', 'cats/{slug}'],
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}