from django.urls import path
from .views import index, home

app_name = 'main'  

urlpatterns = [
    path('', index, name='index'),  # URL untuk halaman depan
    path('home/', home, name='home'),  # URL untuk halaman utama
]
