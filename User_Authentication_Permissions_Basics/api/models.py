from django.db import models
from django.contrib.auth.models import AbstractUser

class Food(models.Model):
    title = models.CharField(max_length=120)
    item_code = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

