from django.contrib import admin
from .models import Registration,Teacher,Subject,Subj_teach,Class_leader, Student_subject
# Register your models here.

admin.site.register(Registration)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Subj_teach)
admin.site.register(Class_leader)
admin.site.register(Student_subject)