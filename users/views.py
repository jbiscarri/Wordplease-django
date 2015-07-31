from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.views.generic import View
from users.forms import LoginForm, SignUpForm


class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')     # Obtengo datos formateados o normalizados
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contrasena incorrecta')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'blog_detail')
                    return redirect(url, user.username)
                else:
                    error_messages.append('El usuario no esta activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('blogs_all')


class SignupView(View):
    def get(self, request):
        error_messages = []
        form = SignUpForm()
        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        error_messages = []
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')     # Obtengo datos formateados o normalizados
            password = form.cleaned_data.get('pwd')
            name = form.cleaned_data.get('name')
            surnames = form.cleaned_data.get('surnames')
            email = form.cleaned_data.get('email')

            if username and password and name and surnames and email:
                User.objects.create_user(username, email=email, password=password, first_name=name, last_name=surnames )
                user = authenticate(username=username, password=password)
                if user is None:
                    error_messages.append('Usuario ya existente')
                else:
                    django_login(request, user)
                    url = request.GET.get('next', 'new_post')
                    return redirect(url)
            else:
                error_messages.append('Faltan datos')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/signup.html', context)
