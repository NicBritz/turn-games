from django.test import TestCase
from games.models import Game
from checkout.models import Order, OrderLineItem
from django.contrib.auth import get_user_model


class TestCheckoutViews(TestCase):
    """ Tests for checkout Views """

    def setUp(self):
        """ Create a temporary user """
        user_model = get_user_model()
        user_model.objects.create_user(
            "bobby", "temporary@gmail.com", "temporary"
        )

    # get checkout page empty cart
    def test_get_empty_checkout_page(self):
        """ Tests for checkout if cart is empty """
        response = self.client.get("/checkout/", follow=True)
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("Your cart is currently empty" in message.message)
        self.assertTemplateUsed(response, "home/index.html")

    # return 404 if url incorrect
    def test_get_checkout_page_404(self):
        response = self.client.get("checkout/afsd")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_get_checkout_success(self):
        """ Tests for checkout success """
        self.client.login(username="bobby", password="temporary")
        temp_game = Game.objects.create(
            name="test_game", description="test_description",
        )
        self.client.get(f"/cart/add/{temp_game.id}", follow=True)
        temp_order = Order.objects.create(
            full_name="test",
            email="test@test.com",
            phone_number="123245",
            street_address1="23 tehioadf",
            town_or_city="hometown",
            postcode="123jdf",
            country="United Kingdom",
        )
        OrderLineItem.objects.create(order=temp_order, game=temp_game)
        response = self.client.get(
            f"/checkout/checkout_success/{temp_order.order_number}",
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Order successfully processed!" in message.message)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
