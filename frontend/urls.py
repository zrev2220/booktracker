from django.urls import path, re_path

from .views import index

urlpatterns = [
    # Default index template to render index.html
    path("", index),
    # Helps Django pass unknown routes to the client-side router
    re_path(r"^.*/$", index),
]
