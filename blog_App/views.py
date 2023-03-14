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
def index(request): 
    contenido ="""
    <html lang="en">

        <head>
            <title>Page Not Found</title>
        </head>

        <body>
            <h1>Page in Development</h1>
        </body>

    </html>
    """    
    return HttpResponse(contenido)

def home(request): 
    noticias = news.objects.all()[:6]
    return render(request,'home.html',{"news":noticias})


def createNew(request):
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            if  request.POST.get('image', False):
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
    new = get_object_or_404(news, id=news_id)
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            if  request.POST.get('image', False):
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
    dt_category=category.objects.all()
    dt_noticias = news.objects.all()
    return render(request,'newsindex.html',{"news":dt_noticias, "categories":dt_category})

def newsView_filter(request, category_id):
    dt_category=category.objects.get(id=category_id)
    dt_noticias = news.objects.filter(categories=dt_category)
    return render(request,'newscategory.html',{"news":dt_noticias, "categories":dt_category})

def newsView_item(request, news_id): 
    titleNews=""
    dt_noticias = news.objects.filter(id=news_id)
    titleNews=dt_noticias[0]
    return render(request,'newsitem.html',{"news":dt_noticias,"titleNews":titleNews})

def deleteNew(request, news_id):
    new = get_object_or_404(news, id=news_id)
    new.delete()
    return redirect('news_table')

def newsTable(request):
    dt_category=category.objects.all()
    dt_noticias = news.objects.filter(author_id=request.user.id)
    return render(request,'news_table.html',{"news":dt_noticias, "categories":dt_category})

def newsTable_Filter(request, category_id):
    dt_categories=category.objects.all()
    dt_category=category.objects.get(id=category_id)
    dt_noticias = news.objects.filter(author_id=request.user.id).filter(categories=dt_category)
    return render(request,'news_table.html',{"news":dt_noticias, "categories":dt_categories})

class RegisterView(CreateView):
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
    template_name='registration/password_change.html'
    success_url=reverse_lazy('password_change_done')

class MyPasswordChangeDoneView(PasswordResetDoneView):
    template_name='registration/password_change_done.html'

# API Views
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = news
        fields = ['title', 'text', 'image', 'categories', 'author']

class NewViewSet(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class = NewSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields = ['name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]