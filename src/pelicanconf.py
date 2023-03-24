AUTHOR = 'Pieter Moens'
SITENAME = 'Pieter Moens'
SITEURL = ''

FAVICON = ''

PLUGIN_PATHS = ['plugins']
PLUGINS = ['resume', 'tailwindcss']

PATH = 'content'
THEME = 'themes/resume'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'LinkedIn', 'https://www.linkedin.com/in/pieter-moens-pimoens/'),
          ('google', 'Google Scholar', 'https://scholar.google.com/citations?user=R6y5jzUAAAAJ'),
          ('orcid', 'ORCID', 'https://orcid.org/0000-0003-2035-8766'),
          ('github', 'GitHub', 'https://github.com/pimoens'),
          ('gitlab', 'GitCoin', 'https://www.gitcoin.co/pimoens'))

DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = []
# TEMPLATE_PAGES = {
#     'resume/resume.html': 'resume.html',
# }

ARTICLE_EXCLUDES = ['resume']
PAGE_EXCLUDES = ['resume']

RESUME_PATH = 'resume'
RESUME_URL = ''
RESUME_SAVE_AS = 'index.html'
ABOUT_SAVE_AS = 'resume/parts/about.html'
EXPERIENCE_SAVE_AS = 'resume/parts/experience.html'
EDUCATION_SAVE_AS = 'resume/parts/education.html'
PUBLICATION_SAVE_AS = 'resume/parts/publications.html'
CERTIFICATE_SAVE_AS = 'resume/parts/certificates.html'
EXTRA_SAVE_AS = 'resume/parts/extras.html'
SKILL_SAVE_AS = 'resume/parts/skills.html'
