from django.test import TestCase
from games.models import Game
from django.contrib.auth import get_user_model


class TestGameViews(TestCase):
    def setUp(self):
        """ Tests for Game Views """
        user_model = get_user_model()
        user_model.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )

    def test_get_all_games_page(self):
        """ get game page response good """
        # filter by All
        response = self.client.get(
            "/games/?category=all&sort=price&direction=asc")
        ctx = response.context.get("sorting")
        self.assertEqual(response.status_code, 200)
        # filter by category
        response = self.client.get(
            "/games/?category=co_op&sort=price&direction=asc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ctx, "price_asc")
        # filter by genre
        response = self.client.get(
            "/games/?genre=action&sort=name&direction=desc")
        ctx = response.context.get("sorting")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ctx, "name_desc")
        # filter by tag
        response = self.client.get("/games/?tag=agriculture")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "games/games.html")
        # filter by discounted
        response = self.client.get(
            "/games/?special_offers=discounted&sort=name&direction=asc"
        )
        self.assertEqual(response.status_code, 200)
        # filter by featured
        response = self.client.get(
            "/games/?special_offers=featured&sort=name&direction=asc"
        )
        self.assertEqual(response.status_code, 200)
        # filter by free
        response = self.client.get(
            "/games/?special_offers=free&sort=name&direction=asc"
        )
        self.assertEqual(response.status_code, 200)
        # filter by query
        response = self.client.get("/games/?q=car")
        self.assertEqual(response.status_code, 200)
        # filter by query no input
        response = self.client.get("/games/?q", follow=True)
        message = list(response.context.get("messages"))[0]
        # no search term provided
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "games/games.html")

    # return 404 if url incorrect
    def test_get_all_games_404(self):
        response = self.client.get("/games/fewt")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    # get game details page response good
    def test_get_game_detail_page(self):
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        response = self.client.get(f"/games/{temp_game.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "games/game_detail.html")

    # rate fail due to not logged in
    # https://stackoverflow.com/questions/16143149/django-testing-check-messages-for-a-view-that-redirects/42252248
    def test_no_login_rate_game(self):
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        response = self.client.get(
            f"/games/rate_game/{temp_game.id}/1/",
            follow=True)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "You must be logged in to "
            "rate this game!" in message.message)
        self.assertTemplateUsed(response, "games/game_detail.html")

    # rate pass when logged in
    # https://stackoverflow.com/questions/7367509/login-in-django-testing-framework
    def test_standard_user_login_rate_game(self):
        self.client.login(username="temporary", password="temporary")
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        # positive rating
        response = self.client.get(
            f"/games/rate_game/{temp_game.id}/1/",
            follow=True)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Added a positive rating!" in message.message)
        self.assertTemplateUsed(response, "games/game_detail.html")
        # negative rating
        response = self.client.get(
            f"/games/rate_game/{temp_game.id}/0/",
            follow=True)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Added a negative rating!" in message.message)
        self.assertTemplateUsed(response, "games/game_detail.html")
        # error rating
        response = self.client.get(
            f"/games/rate_game/{temp_game.id}/g/",
            follow=True)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("No ratings changed!" in message.message)
        self.assertTemplateUsed(response, "games/games.html")
