from django.db import models


# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     desc = models.CharField(max_length=500)
#     price = models.DecimalField(decimal_places=2, max_digits=100000)


class NewsletterSubscription(models.Model):
    full_name = models.CharField(max_length=100)
    e_mail = models.EmailField()

    def __str__(self):
        return self.full_name
