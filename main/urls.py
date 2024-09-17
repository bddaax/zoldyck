from django.urls import path
from main.views import welcome, show_model, create_product_form, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('show_model/', show_model, name='show_model'),
    path('create-product-form', create_product_form, name='create_product_form'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
