from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('request/<user>/', views.request_demo, name='request'),
    path('static/', views.static_demo, name='static'),
]
