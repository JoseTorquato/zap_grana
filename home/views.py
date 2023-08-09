from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone

import logging

from integrations.models import CalledWebHook

logger = logging.getLogger('django')

@login_required(login_url='/login')
def home_view(request):
    try:
        if request.user.profile:
            today = timezone.now().date()
            seven_days_ago = today - timedelta(days=7)

            last_7_days_formatted = [(today - timedelta(days=i)).strftime('%d/%m') for i in range(7)]
            last_7_days_formatted.reverse()
            
            recent_calls = CalledWebHook.objects.filter(
                integration__user_uuid=request.user.profile.uuid,
                created_at__gte=seven_days_ago
            )

            calls_data = {date: 0 for date in last_7_days_formatted}

            for call in recent_calls:
                created_at = call.created_at.astimezone(timezone.utc).strftime('%d/%m')
                calls_data[created_at] += 1

            print(calls_data)
            return render(request, 'index.html', context={"dashboard": {
                "categories": last_7_days_formatted,
                "data": calls_data,
            }})
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