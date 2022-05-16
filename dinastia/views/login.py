from django.contrib.auth import authenticate, login as base_login
from django.contrib.auth import logout as base_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms.login_form import LoginForm


def login(request):
    form = LoginForm()
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if request.GET != {}:
            url = request.GET.get('next') if request.GET['next'] else 'main_menu'
        else:
            url = 'main_menu'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            base_login(request, user)
            return redirect(url)
        else:
            error = 'Неверный логин или пароль'
    return render(request, 'login/login.html', {'form': form,
                                                'error': error})


@login_required
def logout(request):
    base_logout(request)
    return redirect('login')
