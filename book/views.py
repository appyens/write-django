# _*_ encoding utf-8 _*_

""" views for book app """

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Author, Book
from .forms import BookForm, AddLanguageForm


def book_home(request):
    recent = Book.objects.filter(is_active=True).order_by('-created_on')[:3]
    return render(request, 'book/home.html', {'recent': recent, 'total': Book.total_books(), "section": "book"})


@require_GET
def author_list(request):
    if request.method == 'GET':
        all_authors = Author.objects.all
        context = {'authors': all_authors, }
        return render(request, 'book/author_list.html', context)
    return render(request, 'book/author_list.html')


@require_http_methods(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        # getting book objects
        books = Book.objects.filter(is_active=True).order_by('title')
        return render(request, 'book/book_list.html', {'books': books})


def book_by_author(request, author_id=None):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(authors__id=author_id)
    return render(request, 'book/book_list.html', {'books': books, 'author': author})


def book_detail(request, slug_field):
    if request.method == 'GET':
        book = Book.objects.get(slug=slug_field)
        msg = request.session.get('msg', None)
        if msg:
            messages.success(request, msg)
        related_books = Book.objects.filter(genre=book.genre).exclude(title=book.title)
        return render(request, 'book/book_detail.html', {'book': book, 'related': related_books}, status=200)


def search_book(request):
    if request.method == "GET":
        query = request.GET.get('query', None)
        # simple search with title only
        # books = Book.objects.filter(title__icontains=query)
        # advanced lookup with Q
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) |
            Q(authors__first_name__icontains=query) | Q(authors__last_name__icontains=query)
        ).distinct()
        return render(request, 'book/book_list.html', {'books': books, 'query': query}, status=200)


def add_author(request):
    pass


def add_genre(request):
    pass


def add_language(request):
    pass


def add_publisher(request):
    pass


# using model form
@require_http_methods(['GET', 'POST'])
def add_book(request, ):
    template = 'book/add.html'
    context = {}
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            # no need in redirects
            # form = BookForm()
            # return render(request, 'book/add.html', {'form': form})
            request.session.get('success', "Book has been saved successfully")
            return redirect('book:book_detail', slug=book.slug)
    else:
        form = BookForm()
        return render(request, template_name=template, context=context, content_type='text/html', status=200)


@require_http_methods(['GET', 'POST'])
def edit_book(request, pk):
    # book = Book.objects.get(slug=book_slug)
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(book.get_absolute_url())
    return render(request, 'book/edit.html', {'form': form})


@require_POST
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # soft delete
    book.is_active = False
    book.save()
    # hard delete
    # book.delete()
    return redirect('book_list')

#
# def like_book(request):
#     if request.method == 'GET':
#         status = request.GET.get("status")
#         if status == "Like":
#             return JsonResponse({"status": "Unlike"})
#         return JsonResponse({"status": "Like"})
#
#
# def add_language(request):
#     if request.method == "GET":
#         form = AddLanguageForm()
#         return render(request, 'book/add_language.html', {"form": form})
#
#
# @csrf_exempt
# def post_language(request):
#     if request.method == "POST":
#         data = request.POST
#         form = AddLanguageForm()
#         language = form.save(commit=False)
#         language.language = data['data']
#         language.save()
#         return JsonResponse({"status": "Language added successfully"})
