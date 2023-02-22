from django import forms
from django.contrib.auth.models import User
from .models import news

class RegisterForm(forms.Form):
    username = forms.CharField( 
        min_length=4, 
        max_length=30,
        label='Username',
        widget= forms.TextInput(
                attrs= {
                    'placeholder':"Username"
                }
            )
        )
    first_name = forms.CharField (
        min_length =2, 
        max_length = 50,
        widget= forms.TextInput(
                attrs= {
                    'placeholder':'Nombre'
                }
            )
        
        )
    last_name= forms.CharField (
        min_length =2, 
        max_length = 50,
        widget= forms.TextInput(
                attrs= {
                    'placeholder':'Apellido'
                }
            )
        )
    email = forms.CharField(
        min_length=6, 
        max_length= 70, 
        widget=forms.EmailInput(
            attrs= {
                'placeholder':'Email'
                }
            )
        )

    password = forms.CharField (
        max_length = 70, 
        widget=forms.PasswordInput(
                attrs= {
                    'placeholder':'Contraseña'
                }
            )
        )

    confirm_password = forms.CharField (
        max_length =70 , 
        widget=forms.PasswordInput(
                attrs= {
                'placeholder':'Confirmar contraseña'
                }
            )
        )

class NewForm(forms.ModelForm):

    class Meta:
        model = news
        fields = ('title', 'text', 'image', 'categories')

    title = forms.CharField(label='Título:',
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Ingrese un título',
                                    }))
    text = forms.CharField(label='Contenido:', widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'Contenido',
        'rows': 4
    }))
    image = forms.ImageField(label='Imagen:', widget=forms.ClearableFileInput(attrs={
        'class' : 'form-control',

    }))
    # categories = forms.MultipleChoiceField(label="Catgorías:", widget=forms.SelectMultiple(attrs={
    #     'class' : 'form-control'
    # }))
        #title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))