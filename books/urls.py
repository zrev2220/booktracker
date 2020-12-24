from django.urls import path

from books.views import BookAddView, BookEditView, BookDeleteView, BookDetailView, HomePageView, book_search, \
    add_edit_author_ajax, AuthorListView

urlpatterns = [
    path('', HomePageView.as_view(), name='books-search'),
    path('search/', book_search, name='books-search-ajax'),
    path('add/', BookAddView.as_view(), name='book-add'),
    path('details/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('edit/<int:pk>', BookEditView.as_view(), name='book-edit'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('authors/', AuthorListView.as_view(), name='list-authors'),
    path('authors/ajax-form', add_edit_author_ajax, name='author-add-edit')
]
