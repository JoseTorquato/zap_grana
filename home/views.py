from profile import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

@login_required(login_url='/login')
def home_view(request):
    try:
        if request.user.profile:
            return render(request, 'index.html')
    except:    
        return redirect('/profile')
