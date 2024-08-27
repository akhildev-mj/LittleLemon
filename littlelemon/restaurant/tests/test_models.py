from django.test import TestCase
from ..models import Menu


class MenuItemTest(TestCase):
    def test_str_representation(self):
        item = Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(str(item), "Ice Cream : 80")
