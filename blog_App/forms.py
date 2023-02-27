from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import news
class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label='Nombre',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre'
            }
        )
    )

    last_name = forms.CharField(
        label='Apellido',
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellido'
            }
        )
    )
    
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email'
            }
        )
    )
    
    username = forms.CharField(
        min_length=4,
        max_length=30,
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Username"
            }
        )
    )

    password1 = forms.CharField(
        label='Contraseña',
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirmar Contraseña',
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar contraseña'
            }
        )
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                'email', 'password1', 'password2')

class NewForm(forms.ModelForm):

    class Meta:
        model = news
        fields = ('title', 'text', 'image', 'categories')

    title = forms.CharField(label='Título:',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Ingrese un título',
                                }))
    text = forms.CharField(label='Contenido:', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Contenido',
        'rows': 4
    }))
    image = forms.ImageField(label='Imagen:', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
    }))
