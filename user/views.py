from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


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