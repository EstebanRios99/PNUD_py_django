from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewForm, RegisterForm

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
    return render(request,'home.html' )


def createNew(request):
    form = NewForm()
    return render(request, 'create_new.html', {'form': form})

def register(request):
    form = RegisterForm
    return render(request, 'register.html', {'form': form})