from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=1023)
    last_name = models.CharField(max_length=1023)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=127, blank=True)

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
        verbose_name_plural = "People"
