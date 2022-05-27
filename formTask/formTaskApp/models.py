from django.db import models
# Create your models here.


class basicForm(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=None)
    phoneNumber = models.BigIntegerField(max_length=10)
    address = models.TextField(max_length=120)

