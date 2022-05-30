from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inventory'),
    path('/new', views.create_product, name="create_product"),
]
