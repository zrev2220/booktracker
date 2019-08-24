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
from django.contrib import admin
from django.urls import path
from books.views import HomePageView, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='books-search'),
    path('search', search, name='books-search-ajax'),
    # path('logout', ),
    # path('details/<id>', ),
    # path('edit/<id>', ),
    # path('checkout/<id>', ),
    # path('people', ),
    # path('people/add', ),
]

handler400 = "booktracker.views.error400"
handler403 = "booktracker.views.error403"
handler404 = "booktracker.views.error404"
handler500 = "booktracker.views.error500"