from django.urls import path
from .views import (
    AuthorListView, BookCreateView, BookDeleteView, BookDetailView, BookListView,
    BookUpdateView, PublisherListView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("books/add/", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("publishers/", PublisherListView.as_view(), name="publisher-list"),
]
