from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class hospedajeFormulario(forms.Form):
    nombre= forms.CharField()
    habDispo= forms.IntegerField()

class huespedFormulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class reservaFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    fechaDeEntrada= forms.DateField()
    pagado= forms.BooleanField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Ingrese su Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    last_name= forms.CharField()
    first_name= forms.CharField()
    
    class Meta:
        model= User
        fields= ["email","password1", "password2","last_name","first_name"]
        help_texts= {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen= forms.ImageField(required=True)

    class Meta:
        model= User
        fields=["imagen"]
        help_texts= {k:"" for k in fields}