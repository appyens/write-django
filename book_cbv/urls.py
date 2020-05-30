from django.urls import path
from . import views

app_name = 'book_cbv'

urlpatterns = [
    path('home/', views.BookHome.as_view(), name='book_home'),
    path('list/', views.BookListView.as_view(), name='book_list'),
    path('detail/<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),

]
