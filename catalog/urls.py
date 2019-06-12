from .views import *
from django.urls import path


urlpatterns = [
    path('catalog/', catalog_list, name='catalog_list_url'),
    path('catalog/<int:id>/', section_detail, name='category_list_url'),
]
