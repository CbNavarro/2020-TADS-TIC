from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        clean_email = self.cleaned_data['email']

        if User.objects.filter(email=clean_email).exists():
            raise ValidationError('Email ja cadastrado!')

        return clean_email