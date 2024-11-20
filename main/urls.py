from django.urls import path
from .views import show_model, create_product_form, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, add_product_ajax, create_product_flutter
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_model, name='show_model'),
    path('create-product/', views.create_product_form, name='create_product_form'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('edit-product/<uuid:id>/', views.edit_product, name='edit_product'),
    path('delete/<uuid:id>/', views.delete_product, name='delete_product'),
    path('product/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('create-product-ajax/', views.add_product_ajax, name='add_product_ajax'),
    path('create-product-flutter/', views.create_product_flutter, name='create-product-flutter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)