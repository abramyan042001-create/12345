from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField("Имя автора", max_length=160, unique=True)
    biography = models.TextField("Краткая биография", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "автор"
        verbose_name_plural = "авторы"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField("Название издательства", max_length=160, unique=True)
    city = models.CharField("Город", max_length=120, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "издательство"
        verbose_name_plural = "издательства"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("Название книги", max_length=220)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name="books", verbose_name="автор"
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, related_name="books", verbose_name="издательство"
    )
    published_year = models.PositiveSmallIntegerField("Год издания", blank=True, null=True)
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Добавлена", auto_now_add=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})
