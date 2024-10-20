from django.db import models

# Create your models here.

class Student(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    adhar = models.CharField(max_length=255)
    pan = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    heq = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)


