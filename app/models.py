from django.db import models

# Create your models here.

class Registration(models.Model):
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

    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    gender = models.CharField(max_length=10, choices=gender_choices, default=False)
    grade = models.CharField(max_length=10, choices=grade_choices, default=False)
   
   
    def __str__(self):
        return f"{self.first_Name} \n{self.middle_Name} \n{self.last_Name} \n {self.age} \n {self.phone} \n{self.gender} \n{self.grade}"