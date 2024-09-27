from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    catagroy = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(max_length=200)
