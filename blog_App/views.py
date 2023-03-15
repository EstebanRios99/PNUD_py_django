from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from .forms import NewForm, RegisterForm
from django.contrib.auth.models import User
from .models import news, category
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from rest_framework import viewsets, serializers, permissions

# Create your views here.
def home(request): 
    """
    Main View with the most relevant news
    """
    noticias = news.objects.all()[:6]
    return render(request,'home.html',{"news":noticias})


def createNew(request):
    """
    View to create the new news.
    Title, Text and Categories are required
    """
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            print(request.POST, request.FILES)
            if  request.POST.get('image', False) == '':
                new.image = 'blog/noticia_defecto.jpg'
            new.author = request.user
            new.published_date = timezone.now()
            new.save()
            form.save_m2m()
            return redirect('news_table')
        else:
            return render(request, 'create_new.html', {'form': form})
    else:
        form = NewForm()
        return render(request, 'create_new.html', {'form': form})

def updateNew(request, news_id):
    """
    View to edit the old news. You can change the title, description, image and category
    """
    new = get_object_or_404(news, id=news_id)
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            if  request.POST.get('image', False) == '':
                new.image = 'blog/noticia_defecto.jpg'
            new.author = request.user
            new.save()
            form = NewForm()
            return redirect('news_table')
        else:
            return render(request, 'edit_new.html', {'form': form})
    else:
        form = NewForm(instance=new)
        return render(request, 'edit_new.html', {'form': form})

def newsView(request): 
    """
    View to show all news the created.
    """
    dt_category=category.objects.all()
    dt_noticias = news.objects.all()
    return render(request,'newsindex.html',{"news":dt_noticias, "categories":dt_category})

def newsView_filter(request, category_id):
    """
    View to show all the news related to a specific category.
    """
    dt_category=category.objects.get(id=category_id)
    dt_noticias = news.objects.filter(categories=dt_category)
    return render(request,'newscategory.html',{"news":dt_noticias, "categories":dt_category})

def newsView_item(request, news_id): 
    """
    View to show the details of a specific news.
    """
    titleNews=""
    dt_noticias = news.objects.filter(id=news_id)
    titleNews=dt_noticias[0]
    return render(request,'newsitem.html',{"news":dt_noticias,"titleNews":titleNews})

def deleteNew(request, news_id):
    """
    View to delete a specific new.
    """
    new = get_object_or_404(news, id=news_id)
    new.delete()
    return redirect('news_table')

def newsTable(request):
    """
    View to show a table with the news created by a user with the active session.
    """
    dt_category=category.objects.all()
    dt_noticias = news.objects.filter(author_id=request.user.id)
    return render(request,'news_table.html',{"news":dt_noticias, "categories":dt_category})

def newsTable_Filter(request, category_id):
    """
    View to show a table with all the news related to a specific category and a user with the active session.
    """
    dt_categories=category.objects.all()
    dt_category=category.objects.get(id=category_id)
    dt_noticias = news.objects.filter(author_id=request.user.id).filter(categories=dt_category)
    return render(request,'news_table.html',{"news":dt_noticias, "categories":dt_categories})

class RegisterView(CreateView):
    """
    View to register a new user.
    """
    model = User
    form_class = RegisterForm
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('home')

class MyPasswordChangeView(PasswordChangeView):
    """
    View to change the password of a user with the active session.
    """
    template_name='registration/password_change.html'
    success_url=reverse_lazy('password_change_done')

class MyPasswordChangeDoneView(PasswordResetDoneView):
    """
    View to confirm the password change.
    """
    template_name='registration/password_change_done.html'

# API Views
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Api View to query user information.
    (username, email, first_name and last_name)
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserViewSet(viewsets.ModelViewSet):
    """
    Api View to query users information.
    (username, email, first_name and last_name)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = news
        fields = ['title', 'text', 'image', 'categories', 'author']

class NewViewSet(viewsets.ModelViewSet):
    """
    Api View to query news information.
    ('title', 'text', 'image', 'categories', 'author')
    """
    queryset = news.objects.all()
    serializer_class = NewSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields = ['name']

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Api View to query categories information.
    (name)
    """
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]