from django.test import TestCase
from games.models import Game


class TestCartViews(TestCase):
    """ Tests for Cart Views """

    # get cart page response good
    def test_get_view_cart_page(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")

    # return 404 if url incorrect
    def test_get_view_cart_404(self):
        # noinspection SpellCheckingInspection
        response = self.client.get("/cart/afsd")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_add_to_cart(self):
        """ add game to cart """
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        response = self.client.get(f"/cart/add/{temp_game.id}", follow=True)
        self.assertRedirects(response, "/cart/", status_code=301)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue(f"Added {temp_game.name} "
                        f"to your cart!" in message.message)
        self.assertTemplateUsed(response, "cart/cart.html")

    def test_add_to_cart_twice(self):
        """ attempt to add a game twice to cart """
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        self.client.get(f"/cart/add/{temp_game.id}", follow=True)
        response = self.client.get(f"/cart/add/{temp_game.id}", follow=True)
        self.assertRedirects(response, "/cart/", status_code=301)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(f"{temp_game.name} "
                        f"is already in your cart!" in message.message)
        self.assertTemplateUsed(response, "cart/cart.html")

    def test_bad_add_to_cart(self):
        """ add game to cart bad url """
        response = self.client.get("/cart/add/23452332523", follow=True)
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("Error adding item:" in message.message)
        self.assertTemplateUsed(response, "cart/cart.html")

    def test_remove_from_cart(self):
        """ remove game from cart """

        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        response = self.client.get(f"/cart/add/{temp_game.id}", follow=True)
        self.assertRedirects(response, "/cart/", status_code=301)
        # remove game from cart
        response = self.client.get(f"/cart/remove/{temp_game.id}", follow=True)
        # get message from context
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "warning")
        self.assertTrue(f"Removed {temp_game.name} "
                        f"from your cart!" in message.message)
        self.assertTemplateUsed(response, "cart/cart.html")
        # attempt to remove game no longer in cart
        response = self.client.get(f"/cart/remove/{temp_game.id}", follow=True)
        # get new messages
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("Game not found in your cart!" in message.message)
        self.assertTemplateUsed(response, "cart/cart.html")

    # remove game from cart bad url
    def test_bad_remove_from_cart(self):
        response = self.client.get("/cart/remove/559625fgh23", follow=True)
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("Error removing item:" in message.message)
        self.assertTemplateUsed(response, "cart/cart.html")
