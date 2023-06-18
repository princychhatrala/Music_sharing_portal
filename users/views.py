from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
from Music.templates.Music import *

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Music:home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'users/login.html')