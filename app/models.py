from django.db import models

# Create your models here.



gender = ("Gender", "select an option")
male = "Male"
female = "Female"

grade = ("Grade", "select an option")
grade_9 = "Grade 9"
grade_10 = "Grade 10"

gender_choices = [
    gender,
    (male, "Male"),
    (female, "Female")
]

grade_choices = [
    grade,
    (grade_9, "Grade 9"),
    (grade_10, "Grade 10"),
]

class Registration(models.Model):

    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default=False)
    grade = models.CharField(max_length=10, choices=grade_choices, default=False)
   
   
    def __str__(self):
        return self.first_Name

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.subject



class Teacher(models.Model):
    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    phone = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    grade = models.CharField(max_length=10, choices=grade_choices, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_Name
    

class Subj_teach(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teach")
    subject = models.ManyToManyField(Subject,  related_name="sub_teach")





class Class_leader(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="nameing_teacher")
    student = models.ManyToManyField(Registration, related_name="roster")
