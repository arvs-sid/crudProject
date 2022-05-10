from django.db import models

# Create your models here.


class basicForm(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=None)
    phoneNumber = models.CharField(max_length=12)
    address = models.TextField(max_length=120)

