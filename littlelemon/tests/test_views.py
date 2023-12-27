from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza",price=50,inventory=40)
        Menu.objects.create(title="Chicken",price=35,inventory=70)
    
    def test_getall(self):
        pizza = Menu.objects.get(title="Pizza")
        chicken = Menu.objects.get(title="Chicken")
        self.assertEqual(str(pizza), "Pizza : 50.00")
        self.assertEqual(str(chicken), "Chicken : 35.00")