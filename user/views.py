from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user.models import Profile

@login_required(login_url='/login')
def profile_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        setup = Profile(name=name, email=email, phone=phone, user_id=request.user.id)
        setup.save()

    return render(request, 'pages/user/profile.html')
