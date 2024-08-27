from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu
from ..serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Burger", price=5.99, inventory=50)
        self.item2 = Menu.objects.create(title="Pizza", price=8.99, inventory=30)
        self.url = "/restaurant/menu/"

    def test_get_all_menu_items(self):
        response = self.client.get(self.url)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
