from django.db import models

# Create your models here.

# create company model
Types = [
    ('IT', 'Information Technology'),
    ('Finance', 'Finance'),
    ('Healthcare', 'Healthcare'),
    ('Education', 'Education'),
    ('Retail', 'Retail'),
    ('Manufacturing', 'Manufacturing'),
    ('Other', 'Other'),
]

class Company(models.Model):
    name = models.CharField(max_length=50)
    loaction = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=Types)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)