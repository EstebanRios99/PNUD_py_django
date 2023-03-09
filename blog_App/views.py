from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import NewForm, RegisterForm
from django.contrib.auth.models import User
from .models import news, category

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
            if  not request.POST['image']:
                new.image = 'blog/noticia_defecto.jpg'
            new.author = request.user
            new.published_date = timezone.now()
            new.save()
            form.save_m2m()
            return redirect('newsView')
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
            if  not request.POST['image']:
                new.image = 'blog/noticia_defecto.jpg'
            new.author = request.user
            new.save()
            form = NewForm()
            return redirect('newsView')
        else:
            return render(request, 'create_new.html', {'form': form})
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
