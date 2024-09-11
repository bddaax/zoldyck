from django.urls import path
from .views import show_model, welcome

app_name = 'main'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('main/', show_model, name='show_model'),
]
