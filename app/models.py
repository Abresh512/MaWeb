from django.db import models

# Create your models here.
# gender = [
#     ('Male', 'Male'),
#     ('Female', 'Female')
# ]

grade = [
    ('grade_9', '9'),
    ('grade_10', '10')
]

section = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
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
   # gender = models.CharField(max_length=10, choices=gender, default=False)
    grade = models.CharField(max_length=10, choices=grade, default=False)
    section = models.CharField(max_length=2, null=True, choices=section, default=False)
   
    def __str__(self):
        return f"{self.first_Name} {self.last_Name} {self.middle_Name} {self.age}"
    
class Teacher(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    phone = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_Name

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.subject


class Subj_teach(models.Model):
    teacher = models.ManyToManyField(Teacher, related_name="teach")
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE, related_name="sub_teach")
    grade = models.CharField(null=True, blank=True, default=False, max_length=10, choices=grade)
    section = models.CharField(null=True, max_length=2, choices=section)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.teacher} is {self.subject} Teacher."


class Class_leader(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="nameing_teacher")
    grade = models.CharField(null=True, blank=True, default=False, max_length=10, choices=grade)
    student = models.ManyToManyField(Registration, related_name="roster")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.student} is in {self.teacher}"


class Student_subject(models.Model):
    student = models.ManyToManyField(Registration, related_name='student_subject')
    subject = models.ManyToManyField(Subject, related_name='subject_student')
    grade = models.CharField(null=True, blank=True, default=False, max_length=10, choices=grade)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.student}\n {self.subject} \n{self.grade}"


    




# class Section(models.Model):
#     student = models.ManyToManyField(Registration, related_name='student_name')
#     grade = models.CharField(null=True, blank=True, default=False, max_length=10, choices=grade_choices)
#     section = models.CharField(null=False, max_length=2)