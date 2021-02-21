from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def nameValidation(name):
    if len(name)<=1:
        raise ValidationError("Name Must Be at Least 2 Character")
    return name

def contactNoValidator(contact):
    if len(contact)<8 or not contact.isdigit():
        raise ValidationError("Please enter valid contact number")

course= (('csit','BSc.CSIT'),('bca','BCA'),('bit','BIT'))

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=20,validators=[nameValidation,])
    lastname= models.CharField(max_length=20,)
    contactNo=models.CharField(max_length=15,validators=[contactNoValidator,])
    course= models.CharField(max_length=15,choices=course)
    address=models.CharField(max_length=100,null="True",blank="True")
    userid=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
       return self.firstname
