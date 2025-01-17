from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Registration
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                register = form.save()
                return redirect('output')
        else:
            return render(request, 'pages/register.html', {'form':form})
    

def login(request):
    return render(request, 'pages/login.html')


def output(request):
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