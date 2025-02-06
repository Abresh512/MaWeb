from django import forms
from django.forms import ModelForm
from .models import Registration, Teacher


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = ['first_Name', 'middle_Name', 'last_Name', 'age', 'phone', 'username', 'password', 'gender', 'grade', 'section']





# gender = "----"
# male = "Male"
# female = "Female"

# grade = "----"
# grade_9 = "Grade 9"
# grade_10 = "Grade 10"

# gender_choices = [

#     (gender, "----",),
#     (male, "Male"),
#     (female, "Female")
# ]

# grade_choices = [
#     (grade, "----"),
#     (grade_9, "Grade 9"),
#     (grade_10, "Grade 10"),
# ]


# class RegisterForm(forms.ModelForm):
        
#     first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
#     middle_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Middle Name", "class":"form-control"}), label="")
#     last_Name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
#     username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Username", "class":"form-control"}), label="")
#     age = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
#     phone = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")

#     password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={"placeholder":"Password", "class":"form-control"}), label="")        
#     confirm_password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={"placeholder":"Confirm Password", "class":"form-control"}), label="")

#     gender = forms.ChoiceField(choices = gender_choices, required=True, label="Gender", widget=forms.widgets.Select(attrs={"placeholder":"Gender","class":"form-control"}))
#     grade = forms.ChoiceField(choices = grade_choices, required=True, label="Grade", widget=forms.widgets.Select(attrs={"placeholder":"Grade","class":"form-control"}))


#     class Meta:
#         model = Registration
#         fields = ['first_name', 'middle_name', 'last_Name', 'username', 'age', 'phone', 'password', 'confirm_password', 'gender', 'grade']


    '''def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data'''
    

# class login(forms.Form):
#     username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Username", "class":"form-control"}), label="")
#     password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={"placeholder":"Password", "class":"form-control"}), label="")

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         if not username and not password:
#             raise forms.ValidationError('Please enter a username and password')
#         return cleaned_data