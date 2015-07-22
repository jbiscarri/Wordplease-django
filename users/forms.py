__author__ = 'joanbiscarri'
from django import forms

class LoginForm(forms.Form):
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())

class SignUpForm(forms.Form):
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())
    name = forms.CharField(label="Nombre")
    surnames = forms.CharField(label="Apellidos")
    email = forms.EmailField(label="Email")


