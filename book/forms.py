from django import forms
from .models import Book, Author, Language


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'death')


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            'title',
            'authors',
            'edition',
            'pages',
            'year',
            'language',
            'genre',
            'publisher',
            'description',
            'front_cover',
        )
        widgets = {
            'title': forms.TextInput,
            'authors': forms.SelectMultiple,
        }


class AddLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('language',)
