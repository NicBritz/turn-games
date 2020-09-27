from django.test import TestCase
from .models import Game


class TestGameModels(TestCase):

    # test game creation defaults
    def test_game_creation_defaults(self):
        temp_game = Game.objects.create(
            name="test_game", description="test_description",
        )
        self.assertEqual(temp_game.positive_ratings, 0)
        self.assertEqual(temp_game.negative_ratings, 0)
        self.assertEqual(temp_game.price, 0)
        self.assertEqual(temp_game.price_discounted, 0)
        self.assertEqual(temp_game.discount_percent, 0)
        self.assertFalse(temp_game.discounted)
        self.assertFalse(temp_game.featured)
