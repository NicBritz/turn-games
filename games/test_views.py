from django.test import TestCase
from .models import Game
from django.contrib.auth import get_user_model


class TestGameViews(TestCase):
    """ Tests for Game Views """

    def setUp(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )

    # get game page response good
    def test_get_all_games_page(self):
        response = self.client.get("/games/")
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
        response = self.client.get(f"/games/rate_game/{temp_game.id}/1/", follow=True)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("You must be logged in to rate this game!" in message.message)
        self.assertTemplateUsed(response, "games/game_detail.html")

    # rate pass when logged in
    # https://stackoverflow.com/questions/7367509/login-in-django-testing-framework
    def test_standard_user_login_rate_game(self):
        self.client.login(username="temporary", password="temporary")
        temp_game = Game.objects.create(
            name="test_game", description="test_description", price=0
        )
        response = self.client.get(f"/games/rate_game/{temp_game.id}/1/", follow=True)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Added a positive rating!" in message.message)
        self.assertTemplateUsed(response, "games/game_detail.html")
