from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField()
    standard = models.CharField(max_length = 6)
    class Meta:
        db_table = "student"

