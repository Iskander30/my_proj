from django.contrib import admin
from django.urls import path
from .views import index, top-sellers

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', index, name='top-sellers'),
]
