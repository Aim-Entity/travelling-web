from django.db import models


class Location(models.Model):
    image = models.ImageField(width_field=320, height_field=320)
    rating = models.IntegerField()
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=100000)
