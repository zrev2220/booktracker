# TODO remove this tag and this folder
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def app_version():
    return settings.APP_VERSION
