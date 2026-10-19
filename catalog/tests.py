from django.test import TestCase
from django.urls import reverse

from .models import Author, Book, Publisher


class BookCatalogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name="Михаил Булгаков")
        cls.publisher = Publisher.objects.create(name="Художественная литература", city="Москва")
        cls.book = Book.objects.create(
            title="Мастер и Маргарита",
            author=cls.author,
            publisher=cls.publisher,
            published_year=1967,
        )

    def test_home_lists_books_and_related_fields(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Мастер и Маргарита")
        self.assertContains(response, "Михаил Булгаков")
        self.assertContains(response, "Художественная литература")

    def test_search_matches_author(self):
        response = self.client.get(reverse("book-list"), {"q": "Булгаков"})
        self.assertContains(response, "Мастер и Маргарита")

    def test_create_book_view_saves_foreign_keys(self):
        response = self.client.post(reverse("book-create"), {
            "title": "Собачье сердце",
            "author": self.author.pk,
            "publisher": self.publisher.pk,
            "published_year": 1925,
            "description": "Повесть",
        })
        self.assertRedirects(response, reverse("book-detail", kwargs={"pk": Book.objects.latest("pk").pk}))
        self.assertTrue(Book.objects.filter(title="Собачье сердце", author=self.author, publisher=self.publisher).exists())

    def test_detail_shows_author_and_publisher(self):
        response = self.client.get(reverse("book-detail", kwargs={"pk": self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.publisher.name)
