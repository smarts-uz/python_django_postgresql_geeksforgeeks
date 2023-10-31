from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Employee

# Employee.objects.create(name='test2',contact='44453953')

# def some_name(request):
#     employee_instance = Employee.objects.create(name='test1',contact='453953')
#     return render(request, 'some_name.html.html')

# Create your views here.

def addStudent(request):
    form = Employee
    context = {'form':form}
    return render(request, 'accounts/add-student.html', context)