"""booktracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from cra_helper.views import proxy_cra_requests

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("frontend.urls")),
]

handler400 = "booktracker.errorviews.error400"
handler403 = "booktracker.errorviews.error403"
handler404 = "booktracker.errorviews.error404"
handler500 = "booktracker.errorviews.error500"

# add a reverse-proxy view to help React in the Django view talk to Create-React-App
if settings.DEBUG:
    proxy_urls = [
        re_path(r"^__webpack_dev_server__/(?P<path>.*)$", proxy_cra_requests),
        re_path(r"^(?P<path>.+\.hot-update\.(js|json|js\.map))$", proxy_cra_requests),
    ]
    urlpatterns.extend(proxy_urls)
