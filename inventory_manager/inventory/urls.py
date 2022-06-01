from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inventory'),
    path('new', views.create_product, name="create_product"),
    path('edit/<int:id>', views.edit_product, name="edit_product"),
    path('delete/<int:id>', views.delete_product, name="delete_product"),
    path('update_status/<int:id>-<str:status_name>', views.update_product_status, name="update_product_status"),
]
