from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name, self.email
