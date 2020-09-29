from django.test import TestCase
from profiles.forms import UserProfileForm


class TestUserProfileForms(TestCase):
    def test_profile_fields_in_meta(self):
        """ check if correct fields are in Metaclass """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ("user",))

    def test_profile_valid_form(self):
        form = UserProfileForm(
            {
                "default_phone_number": "123245",
                "default_street_address1": "23 tehioadf",
                "default_town_or_city": "hometown",
                "default_postcode": "123jdf",
                "default_country": "US",
            }
        )
        self.assertTrue(form.is_valid())
