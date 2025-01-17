from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Registration
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('output')
        
    return render(request, 'pages/register.html', {'form':form})

def login(request):
    return render(request, 'pages/login.html')


def output(request):
    if request.user.is_authenticated:
        records = Registration.objects.all()
        if request.method == 'post':
            username = request.POST.get['username']
            password = request.POST.get['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('output')
            else:
                return redirect('index')
        return render(request, 'pages/output.html', {'records':records})
    return redirect('index')