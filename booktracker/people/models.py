from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=1023)
    last_name = models.CharField(max_length=1023)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=127, blank=True)
