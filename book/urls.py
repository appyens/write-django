from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    # display
    path('home/', views.book_home, name='book_home'),
    path('list/', views.book_list, name='book_list'),
    path('list/authors/', views.author_list, name='authors_list'),
    path('author/<int:author_id>/', views.book_by_author, name='by_author'),
    path('detail/<slug:slug_field>/', views.book_detail, name='book_detail'),
    path('search_book/', views.search_book, name='search_book'),
    # edit
    path('add/', views.add_book, name='add_book'),
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    # ajax
    # path('like/', views.like_book, name="like_book"),
    # path('language/add/', views.add_language, name='add_lang'),
    # path('language/post/', views.post_language, name='post_lang'),

]
