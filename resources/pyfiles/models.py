from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    education_field = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"