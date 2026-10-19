from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import BookForm
from .models import Author, Book, Publisher


class BookListView(ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "books"
    paginate_by = 12

    def get_queryset(self):
        queryset = Book.objects.select_related("author", "publisher")
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(author__name__icontains=query)
                | Q(publisher__name__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        context["total_books"] = Book.objects.count()
        context["total_authors"] = Author.objects.count()
        context["total_publishers"] = Publisher.objects.count()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"
    queryset = Book.objects.select_related("author", "publisher")


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"
    extra_context = {"page_title": "Новая книга", "submit_label": "Добавить книгу"}

    def form_valid(self, form):
        messages.success(self.request, "Книга добавлена в каталог.")
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"
    extra_context = {"page_title": "Редактирование книги", "submit_label": "Сохранить изменения"}

    def form_valid(self, form):
        messages.success(self.request, "Изменения сохранены.")
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    template_name = "catalog/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        messages.success(self.request, "Книга удалена из каталога.")
        return super().form_valid(form)


class AuthorListView(ListView):
    model = Author
    template_name = "catalog/author_list.html"
    context_object_name = "authors"

    def get_queryset(self):
        return Author.objects.prefetch_related("books")


class PublisherListView(ListView):
    model = Publisher
    template_name = "catalog/publisher_list.html"
    context_object_name = "publishers"

    def get_queryset(self):
        return Publisher.objects.prefetch_related("books")
