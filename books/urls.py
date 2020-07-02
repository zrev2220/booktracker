from django.urls import path

from books.views import AddBookView, EditBookView, DeleteBookView, BookDetailView, HomePageView, book_search, \
    add_author_ajax

urlpatterns = [
    path('', HomePageView.as_view(), name='books-search'),
    path('search/', book_search, name='books-search-ajax'),
    path('add/', AddBookView.as_view(), name='add-book'),
    path('details/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('edit/<int:pk>', EditBookView.as_view(), name='edit-book'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='delete-book'),
    path('authors/add-ajax', add_author_ajax, name='add-author')
]
