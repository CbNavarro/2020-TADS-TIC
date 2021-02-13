from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
