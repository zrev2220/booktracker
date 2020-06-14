from unittest import TestCase

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
