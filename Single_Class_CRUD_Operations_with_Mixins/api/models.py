from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=120)
    item_code = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
