from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    message = models.CharField(max_length=500, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return f"This is {self.first_name}"