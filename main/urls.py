from django.urls import path
from .views import show_model 

app_name = 'main'

urlpatterns = [
    path('', show_model, name='show_model'),
]
