from django.db import models

# Create your models here.

class Applicants(models.Model):
    fname = models.CharField("fname", max_length=255)
    gender = models.CharField("gender", max_length=255)
    city =  models.CharField("city", max_length=255)
    
