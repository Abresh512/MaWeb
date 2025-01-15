from django import forms


    
gender = "----"
male = "Male"
female = "Female"

grade = "----"
grade_9 = "Grade 9"
grade_10 = "Grade 10"

gender_choices = [

    (gender, "----",),
    (male, "Male"),
    (female, "Female")
]

grade_choices = [
    (grade, "----"),
    (grade_9, "Grade 9"),
    (grade_10, "Grade 10"),
]


class RegisterForm(forms.Form):
    first_Name = forms.CharField(max_length=255)
    middle_Name = forms.CharField(max_length=255)
    last_Name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    phone = forms.IntegerField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    
    
    gender_choices = forms.ChoiceField(choices = gender_choices, required=True, label="Gender")
    grade_choices = forms.ChoiceField(choices = grade_choices, required=True, label="Grade")


    '''def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data'''
    