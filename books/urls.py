from django.urls import path

from books.views import AddBookView, HomePageView, book_search

urlpatterns = [
    path('', HomePageView.as_view(), name='books-search'),
    path('search', book_search, name='books-search-ajax'),
    path('add', AddBookView.as_view(), name='add-book'),
    # path('details/<id>', ),
    # path('edit/<id>', ),
]
