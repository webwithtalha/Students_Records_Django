from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField()
    dob = models.DateField()



