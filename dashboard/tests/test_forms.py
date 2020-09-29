from django.test import TestCase
from dashboard.forms import GameForm


class TestDashboardForms(TestCase):
    def test_fields_in_meta(self):
        """ check if correct fields are in Metaclass """
        form = GameForm()
        self.assertEqual(
            form.Meta.fields,
            (
                "name",
                "header_image_url",
                "release_date",
                "developer",
                "publisher",
                "platforms",
                "price",
                "discount_percent",
                "categories",
                "genres",
                "featured",
                "discounted",
                "tags",
                "description",
            ),
        )

    def test_required_fields(self):
        """ check if correct fields are required """
        form = GameForm({"name": "", "description": "", "price": "", })
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_valid_form(self):
        form = GameForm({"name": "test", "description": "test data", "price": "10.00", })
        self.assertTrue(form.is_valid())
