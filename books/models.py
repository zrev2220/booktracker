from django.db import models
from people.models import Person


class Author(models.Model):
    first_name = models.CharField(max_length=1023, blank=True)
    last_name = models.CharField(max_length=1023)

    def __str__(self):
        return " ".join((self.first_name, self.last_name))


class Category(models.Model):
    code = models.CharField(max_length=5, unique=True)
    descr = models.CharField(max_length=1023)

    def __str__(self):
        return self.descr


class Book(models.Model):
    title = models.CharField(max_length=2047)
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    return_date = models.DateField(blank=True, null=True)
    author = models.ManyToManyField(Author, blank=True)
    category = models.ManyToManyField(Category)
    checkout = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

