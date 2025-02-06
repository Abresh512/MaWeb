from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Registration, Teacher, Subj_teach, section
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')



def register(request):
    submitted = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'pages/register.html', 
        {'form':form, 
        'submitted':submitted,
        })



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('students')
        else:
            return redirect('login')
    return render(request, 'pages/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')


def students(request):
    if request.user.is_authenticated:
        records = Registration.objects.all()
        if request.method == 'post':
            username = request.POST.get['username']
            password = request.POST.get['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('students')
            else:
                return redirect('index')
        return render(request, 'pages/students.html', {'records':records})
    return redirect('index')



def teachers(request):
    if request.user.is_authenticated:
        records = Teacher.objects.all()
        if request.method == 'post':
            username = request.POST.get['username']
            password = request.POST.get['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('teachers')
            else:
                return redirect('index')
        return render(request, 'pages/teachers.html', {'records':records})
    return redirect('index')



def sub_teach(request):
    if request.user.is_authenticated:
        records = Subj_teach.objects.all()
        return render(request, 'pages/sub_teach.html', {'records':records})
    return render('index')


def section_A(request):
    if request.user.is_authenticated:
        records = Registration.objects.filter(section='A')
        return render(request, 'pages/grade9.html',
            {'records':records})
    
def section_A(request):
    if request.user.is_authenticated:
        records = Registration.objects.filter(section='A')
        return render(request, 'pages/grade9.html',
            {'records':records})