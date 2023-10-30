from django.contrib import admin

# Register your models here.
from myapp.models import StudentForm, Employee

admin.site.register(StudentForm)  # StudentForm is registered
admin.site.register(Employee)  # Employee is registered