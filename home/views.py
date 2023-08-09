from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import logging

logger = logging.getLogger('django')

@login_required(login_url='/login')
def home_view(request):
    try:
        # logger.warning(request.user.profile)
        if request.user.profile:
            return render(request, 'index.html')
    except Exception as e:
        print(e)    
        return redirect('/profile')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('/')
        messages.error(request, "Email ou senha inválidos. Por favor, tente novamente.")
        return redirect('login')
    return render(request, 'auth/login.html')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')