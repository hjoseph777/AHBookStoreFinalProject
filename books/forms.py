from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'rating', 'description']  # exclude user - we'll set that in the view
        # could add some custom widgets here later if needed