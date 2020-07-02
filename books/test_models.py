from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase

from books.models import Author


class TestAuthor(TestCase):
    def test_get_full_name(self):
        a1 = Author(first_name="Foo", last_name="Bar")
        self.assertEqual("Foo Bar", a1.get_full_name())
        self.assertEqual("Bar, Foo", a1.get_full_name(True))
        a2 = Author(first_name="Foo")
        self.assertEqual("Foo", a2.get_full_name())
        self.assertEqual("Foo", a2.get_full_name())
        a3 = Author(last_name="Bar")
        self.assertEqual("Bar", a3.get_full_name())
        self.assertEqual("Bar", a3.get_full_name())

    def test_unique_names(self):
        Author.objects.create(first_name="Foo", last_name="Bar")
        with self.assertRaises(IntegrityError), transaction.atomic():
            Author.objects.create(first_name="Foo", last_name="Bar")
        Author.objects.create(first_name="Foo", last_name="Baz")
        Author.objects.create(first_name="Phooey", last_name="Bar")

    def test_blank_names(self):
        with self.assertRaises(ValidationError), transaction.atomic():
            Author(first_name="Foo", last_name="").full_clean()
        Author(first_name="", last_name="Bar").full_clean()
        Author(last_name="Bar").full_clean()
        with self.assertRaises(ValidationError), transaction.atomic():
            Author(first_name="Foo").full_clean()
