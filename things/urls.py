from django.urls import path
from .views import one, two, three

urlpatterns = [
    path('one/', one, name='one'),
    path('two/', one, name='two'),
    path('three/', one, name='three'),
]
