"""
Django *production* settings for booktracker project.
Imports all settings from settings.py, then overrides various options
"""

# import os
# import dj_database_url
import django_heroku

# Import from development settings
try:
    from .settings import *
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = False

ALLOWED_HOSTS = ['*'] if DEBUG else []

django_heroku.settings(locals())

# Connect to database with Heroku's DATABASE_URL env var
# DATABASES['default'] = dj_database_url.config(os.getenv('DATABASE_URL'))  # Not used b/c using django-heroku module
