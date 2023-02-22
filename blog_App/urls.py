from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('create/new', views.createNew, name='create_new'),
    path('register', views.register, name='register')
]