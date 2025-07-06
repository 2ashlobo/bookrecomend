from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'description', 'genre', 'rating']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
        }
