from django.contrib import admin
from .models import Author, Book, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "published_year")
    list_filter = ("publisher", "published_year")
    search_fields = ("title", "author__name", "publisher__name")
    autocomplete_fields = ("author", "publisher")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ("name",)
