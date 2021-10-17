from django.db import models


#class models to manage information from the database inside of python
# Create your models here.
class Feature(models.Model):
    name =  models.CharField(max_length=100, default="feature1")
    details = models.CharField(max_length=150, default="type your description")