from django.contrib import admin 
from django.db import models 
class Contact(models.Model): 
    name = models.CharField(max_length=200) 
    firstname = models.CharField(max_length=200) 
    email = models.EmailField(max_length=200) 
    message = models.CharField(max_length=1000) 
def __str__(self): 
    return f"{self.name} {self.firstname} ({self.email})" 
