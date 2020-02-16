#foo/apps.py

from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'full.python.path.to.your.app.blog'
    label = 'my.blog'

default_app_config = 'full.python.path.to.your.app.blog.apps.BlogConfig'