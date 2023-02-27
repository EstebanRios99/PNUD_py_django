from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    # Noticias
    path('create/new', views.createNew, name='create_new'),
    path('save/new', views.saveNew, name='saveNew'),
    # Usuarios
    path('login', LoginView.as_view(),name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('register', views.RegisterView.as_view(), name='register')
]
