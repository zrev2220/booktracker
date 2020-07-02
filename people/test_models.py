from django.test import TestCase

from people.models import Person


class TestPerson(TestCase):
    def test_get_full_name(self):
        p1 = Person(first_name="Foo", last_name="Bar")
        self.assertEqual("Foo Bar", p1.get_full_name())
        self.assertEqual("Bar, Foo", p1.get_full_name(True))
        p2 = Person(first_name="Foo")
        self.assertEqual("Foo", p2.get_full_name())
        self.assertEqual("Foo", p2.get_full_name())
        p3 = Person(last_name="Bar")
        self.assertEqual("Bar", p3.get_full_name())
        self.assertEqual("Bar", p3.get_full_name())
