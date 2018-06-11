from django.db import models
import datetime

class School(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)

class Student(models.Model):
    school = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)