from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = login(request, user)
            return redirect('blog:home')
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/signup.html', {'form': form})


def guest_login(request):
    user, created = User.objects.get_or_create(username='Guest')
    user = login(request, user)
    redirect_url = request.GET.get('next','blog:home')
    print(redirect_url)
    redirect_url = 'blog:home' if redirect_url in [None, ''] else redirect_url
    return redirect(redirect_url)