from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', views.post_detail, name='post_detail'),
    path('share/<int:post_id>', views.share_post, name='share_post'),
    path('search/', views.search_post, name='search_post'),

]