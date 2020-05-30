# _*_ encoding utf-8 _*_

""" views for book app """

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages

from .models import Author, Book


class BookHome(TemplateView):
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        context = super(BookHome, self).get_context_data(**kwargs)
        context['recent'] = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
        context['total'] = Book.total_books()
        return context


class BookListView(ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        book = self.object
        context['related'] = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        context['success'] = self.request.session.get('success', None)
        print(context)
        return context


class BookEditView(UpdateView):
    pass


class BookDeleteView(DeleteView):
    pass
