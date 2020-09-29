from django.test import TestCase
from games.models import Game, Category, Genre, Tag


class TestGameModels(TestCase):
    def test_game_creation_defaults(self):
        """ tests the game creation defaults"""
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

    def test_game_string_method(self):
        """ test the game string """
        temp_game = Game.objects.create(
            name="test_game", description="test_description",
        )
        self.assertEqual(str(temp_game), "test_game")

    def test_category_string_method(self):
        """ test the category strings """
        temp_category = Category.objects.create(
            name="test_category", friendly_name="test category",
        )
        self.assertEqual(str(temp_category), "test_category")
        self.assertEqual(str(
            temp_category.get_friendly_name()), "test category")

    def test_genre_string_method(self):
        """ test the genre strings """
        temp_genre = Genre.objects.create(
            name="test_genre", friendly_name="test genre",
        )
        self.assertEqual(str(temp_genre), "test_genre")
        self.assertEqual(str(temp_genre.get_friendly_name()), "test genre")

    def test_tag_string_method(self):
        """ test the tag strings """
        temp_tag = Tag.objects.create(
            name="test_tag", friendly_name="test tag",
        )
        self.assertEqual(str(temp_tag), "test_tag")
        self.assertEqual(str(temp_tag.get_friendly_name()), "test tag")
