from django.db import models


# Create your models here.
class StudentForm(models.Model):
    firstname = models.CharField("Enter first name", max_length=50)
    lastname = models.CharField("Enter last name", max_length=50)
    email = models.EmailField("Enter Email")
    file = models.FileField()  # for creating file input

    class Meta:
        db_table = "student"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"