from django.urls import path
from .views import index, home

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
]
