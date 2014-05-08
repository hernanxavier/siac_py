# coding=utf-8
__author__ = 'xavier'
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class Registro_Usuario(forms.Form):
    """
        Formulario para registrar nuevos usuarios en el sistema
    """

    usuario = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input username', 'placeholder': 'Nombre de usuario'}))
    nombre = forms.CharField(max_length=200,
                             widget=forms.TextInput(attrs={'class': 'input username', 'placeholder': 'Nombres'}))
    apellido = forms.CharField(max_length=200,
                               widget=forms.TextInput(attrs={'class': 'input username', 'placeholder': 'Apellidos'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input username', 'placeholder': 'email@dominio.com'}))
    passwd1 = forms.CharField(max_length=16,
                              widget=forms.PasswordInput(attrs={'class': 'input password', 'placeholder': 'Password'}))
    passwd2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'input password', 'placeholder': 'Confirmar Password'}))

    def clean_usuario(self):
        """
            Valida que el nombre de usuario no swe repita
        """
        usuario = self.cleaned_data['usuario']
        if User.objects.filter(username=usuario).count():
            raise forms.ValidationError(u'El usuario "%s" ya está en uso.' % usuario)
        return usuario

    def clean_email(self):
        """
            Valida que el nombre de usuario no swe repita
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count():
            raise forms.ValidationError(u'El correo "%s" ya está registrado.' % email)
        return email

    def clean_passwd1(self):
        """
            Función que valida el numero de caracteres de la contraseña (>4, <6)
        """

        passwd1 = self.cleaned_data.get('passwd1', '')
        num_letters = len(passwd1)
        if num_letters < 4:
            raise forms.ValidationError('Su contraseña debe tener entre 4 y 16 caracteres')
        return passwd1

    def clean_passwd2(self):
        """
            Función que valida que el primer y el segundo password sean iguales
        """

        passwd1 = self.cleaned_data.get('passwd1', '')
        passwd2 = self.cleaned_data.get('passwd2', '')
        if passwd1 != passwd2:
            raise forms.ValidationError('Los passwords no coinciden')
        return passwd2

