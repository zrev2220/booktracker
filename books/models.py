from django.core.exceptions import ValidationError
from django.db import models
from people.models import Person


class Author(models.Model):
    first_name = models.CharField(max_length=1023, blank=True)
    last_name = models.CharField(max_length=1023)

    def clean(self):
        # Require non-empty last name
        if self.last_name is None or len(self.last_name) == 0:
            raise ValidationError("Author last name must be non-blank")

    def get_full_name(self, reverse=False):
        if reverse:
            return ", ".join(
                [name for name in (self.last_name, self.first_name) if name]
            )
        else:
            return " ".join(
                [name for name in (self.first_name, self.last_name) if name]
            )

    def __str__(self):
        return self.get_full_name()

    class Meta:
        unique_together = ("first_name", "last_name")


class Category(models.Model):
    code = models.CharField(max_length=5, unique=True)
    descr = models.CharField(max_length=1023)

    def __str__(self):
        return self.descr

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=2047)
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    return_date = models.DateField(blank=True, null=True)
    author = models.ManyToManyField(Author, blank=True)
    category = models.ManyToManyField(Category)
    checkout = models.ForeignKey(
        Person, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.title
