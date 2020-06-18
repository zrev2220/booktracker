from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView


class MyLoginView(LoginView):
    template_name = "login.html"
