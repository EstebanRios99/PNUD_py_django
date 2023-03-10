from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    # Noticias
    path('news', views.newsView, name='newsView'),
    path('news/category/<int:category_id>/', views.newsView_filter, name="category"),
    path('news/newsitem/<int:news_id>/', views.newsView_item, name="newsitem"),
    path('create/new', views.createNew, name='create_new'),
    path('update/new/<int:news_id>', views.updateNew, name='update_new'),
    path('delete/new/<int:news_id>', views.deleteNew, name='delete_new'),
    # Usuarios
    path('login', LoginView.as_view(),name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('register', views.RegisterView.as_view(), name='register')
]
