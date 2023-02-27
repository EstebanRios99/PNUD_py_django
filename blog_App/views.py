from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import NewForm, RegisterForm
from django.contrib.auth.models import User

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
    return render(request,'home.html')


def createNew(request):
    form = NewForm()
    return render(request, 'create_new.html', {'form': form})

def saveNew(request):
    form = NewForm(request.POST, request.FILES)
    if form.is_valid():
        new = form.save(commit=False)
        new.author = request.user
        new.published_date = timezone.now()
        new.save()
        form = NewForm()
    
    return render(request, 'create_new.html', { 'form' : form, 'message' : 'ok'})

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
    