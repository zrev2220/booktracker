"""
Django *production* settings for booktracker project.
Imports all settings from settings.py, then overrides various options
"""

import django_heroku

# Import from development settings
try:
    from .settings import *  # noqa: F401,F403
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = False

ALLOWED_HOSTS = ["*"] if DEBUG else []

django_heroku.settings(locals())
