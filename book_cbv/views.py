# _*_ encoding utf-8 _*_

""" views for book app """

from django.views import generic
from django.contrib import messages

from .models import Author, Book


class BookHome(generic.TemplateView):
    template_name = 'book_cbv/home.html'

    def get_context_data(self, **kwargs):
        context = super(BookHome, self).get_context_data(**kwargs)
        context['recent'] = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
        context['total'] = Book.total_books()
        return context


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        book = self.object
        context['related'] = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        context['success'] = self.request.session.get('success', None)
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        pass


class BookEditView(generic.UpdateView):
    pass


class BookDeleteView(generic.DeleteView):
    pass
