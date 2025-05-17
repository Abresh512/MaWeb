from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('students', views.Principal, name='students'),
    path('<str:pk>/User', views.student, name="user"),
    path('teachers', views.teachers, name="teachers"),
    path('sub_teach', views.sub_teach, name='sub_teach'),

    path('grade', views.Grade, name='grade'),
    path('grade9', views.grade_9, name="grade9"),
    path('grade10', views.grade_10, name="grade10"),

    path("addmark", views.newMark, name="newmark"),
    path("marklist", views.markList, name="marklist"),

]