from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views
from rest_framework import routers
from blog_App.views import UserViewSet, NewViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('news', NewViewSet)
router.register('category-detail', CategoryViewSet)

urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='home'),
    # Noticias
    path('news', views.newsView, name='newsView'),
    path('news/category/<int:category_id>/', views.newsView_filter, name="category"),
    path('news/newsitem/<int:news_id>/', views.newsView_item, name="newsitem"),
    path('create/new', login_required(views.createNew), name='create_new'),
    path('update/new/<int:news_id>', login_required(views.updateNew), name='update_new'),
    path('delete/new/<int:news_id>', login_required(views.deleteNew), name='delete_new'),
    path('news/table', login_required(views.newsTable), name='news_table'),
    path('news/table/<int:category_id>', login_required(views.newsTable_Filter), name='news_tableCategory'),
    # Usuarios
    path('login', LoginView.as_view(),name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('change_password', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('change_password/done', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),

    # Api
    path('api/', include(router.urls))

]
