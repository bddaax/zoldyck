from django.urls import path
from .views import welcome, show_model  

app_name = 'main'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('show_model/', show_model, name='show_model'),
]
