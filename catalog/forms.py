from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publisher", "published_year", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Например, Мастер и Маргарита"}),
            "published_year": forms.NumberInput(attrs={"min": 1, "max": 2100, "placeholder": "Например, 1967"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Краткое описание книги"}),
        }
