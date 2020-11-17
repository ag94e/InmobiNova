from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formContacto(forms.Form):

    asunto = forms.CharField()
    mail = forms.EmailField()
    mensaje = forms.CharField()


class crearUsuario(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email"]
