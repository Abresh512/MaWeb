from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
        

def allowed_user(allowedUsers=[]):
    def decoretors(view_func):
        def wrapper_func(request, *args, **kwargs):
        
            print('working', allowedUsers)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowedUsers:
                return view_func(request, *args, **kwargs)
            
            else:
                return HttpResponse("You're not allowed! ")
        return wrapper_func
    return decoretors

