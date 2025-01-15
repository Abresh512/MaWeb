from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Registration
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('output')
    else:
        form = RegisterForm()
        return render(request, 'pages/register.html', {
            'form': form})
    

def login(request):
    return render(request, 'pages/login.html')


def output(request):
    return render(request, 'pages/output.html', {
        'output': Registration.objects.all()})