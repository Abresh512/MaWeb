from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, NewMarkk
from .models import Registration, Teacher, Subj_teach, NewMark
from .decorator import unauthenticated_user,allowed_user
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

@login_required(login_url='login')
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


@unauthenticated_user
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


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
@allowed_user(allowedUsers=['Principal'])
def Principal(request):
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


@allowed_user(allowedUsers=['students'])
@login_required(login_url='login')
def student(request, pk):
        user = Registration.objects.get(id=pk)
        context = {'user':user}
        return render(request, 'pages/user.html', context)



@login_required(login_url='login')
def teachers(request):
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



@login_required(login_url='login')
@allowed_user(allowedUsers=['Principal'])
def sub_teach(request):
        records = Subj_teach.objects.all()
        return render(request, 'pages/sub_teach.html', {'records':records})


@login_required(login_url='login')
def newMark(request):
    records = Registration.objects.all()
    record = NewMark.objects.all()
    form = NewMarkk(request.POST or None)
    if form.is_valid():
         form.save()
         return redirect('marklist')
    context = {'records':records, 'record':record, 'form':form}
    return render(request, "pages/newmark.html", context)

@login_required(login_url='login')
def markList(request):
    records = Registration.objects.all()
    marklist = NewMark.objects.all()
    form = NewMarkk()
    context = {'records':records, 'record':marklist, 'form':form}
    return render(request, "pages/marklist.html", context)



@login_required(login_url='login')
def Grade(request):
    return render(request, 'pages/grade.html')



@login_required(login_url='login')
def grade_9(request):
        sectiona = Registration.objects.filter(grade__in=['grade_9'], section__in=['A'])
        sectionb = Registration.objects.filter(grade__in=['grade_9'], section__in=['B'])
        sectionc = Registration.objects.filter(grade__in=['grade_9'], section__in=['C'])
        
        context = {
            'recorda':sectiona,
            'recordb':sectionb,
            'recordc':sectionc

        }
        return render(request, 'pages/grade9.html', context)
    
   
@login_required(login_url='login')
def grade_10(request):
        sectiona = Registration.objects.filter(grade__in=['grade_10'], section__in=['A'])
        sectionb = Registration.objects.filter(grade__in=['grade_10'], section__in=['B'])
        sectionc = Registration.objects.filter(grade__in=['grade_10'], section__in=['C'])
        
        context = {
            'recorda':sectiona,
            'recordb':sectionb,
            'recordc':sectionc

        }
        return render(request, 'pages/grade10.html', context)
    
