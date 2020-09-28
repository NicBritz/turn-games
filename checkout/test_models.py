from django.test import TestCase
from .models import Order, OrderLineItem
from games.models import Game
from decimal import Decimal


class TestCheckoutModels(TestCase):
    def test_Order_creation_defaults(self):
        """ Tests adding an order """
        temp_order = Order.objects.create(
            full_name="test",
            email="test@test.com",
            phone_number="123245",
            street_address1="23 tehioadf",
            town_or_city="hometown",
            postcode="123jdf",
            country="United Kingdom",
        )
        self.assertEqual(temp_order.full_name, "test")
        self.assertEqual(temp_order.stripe_pid, "")
        self.assertEqual(temp_order.original_cart, "")
        self.assertEqual(temp_order.order_total, 0)
        self.assertEqual(temp_order.grand_total, 0)

    def test_order_line_item_add(self):
        """ Tests adding a line item """
        # src: https://stackoverflow.com/questions/17314028/compare-decimals-in-python
        # sets decimal to 2 places for testing
        two_dec_places = Decimal(10) ** -2
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=Decimal(23.99)
        )

        temp_order = Order.objects.create(
            full_name="test",
            email="test@test.com",
            phone_number="123245",
            street_address1="23 tehioadf",
            town_or_city="hometown",
            postcode="123jdf",
            country="United Kingdom",
        )
        temp_line_item = OrderLineItem.objects.create(order=temp_order, game=temp_game)
        self.assertEqual(temp_line_item.line_item_total.quantize(two_dec_places), temp_game.price.quantize(two_dec_places))
        self.assertEqual(temp_line_item.order.order_number, temp_order.order_number)
        self.assertEqual(temp_line_item.order.line_items.count(), 1)
