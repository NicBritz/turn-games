from django.test import TestCase
from checkout.forms import OrderForm


class TestCheckoutForms(TestCase):
    def test_fields_in_meta(self):
        """ check if correct fields are in Metaclass """
        form = OrderForm()
        self.assertEqual(
            form.Meta.fields,
            (
                "full_name",
                "email",
                "phone_number",
                "street_address1",
                "street_address2",
                "town_or_city",
                "postcode",
                "county",
                "country",
            ),
        )

    def test_required_fields(self):
        """ check if correct fields are required """
        form = OrderForm(
            {
                "full_name": "",
                "email": "",
                "phone_number": "",
                "street_address1": "",
                "town_or_city": "",
                "postcode": "",
                "country": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors.keys())
        self.assertEqual(form.errors["full_name"][0], "This field is required.")

    def test_valid_form(self):
        form = OrderForm(
            {
                "full_name": "test",
                "email": "test@test.com",
                "phone_number": "123245",
                "street_address1": "23 tehioadf",
                "town_or_city": "hometown",
                "postcode": "123jdf",
                "country": "US",
            }
        )
        self.assertTrue(form.is_valid())
