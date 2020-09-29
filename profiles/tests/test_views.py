from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import UserProfile
from checkout.models import Order


class TestProfileViews(TestCase):
    """ Tests for Profile Views """

    def setUp(self):
        """ Create a temporary user """
        user_model = get_user_model()
        user_model.objects.create_user(
            "bobby", "temporary@gmail.com", "temporary"
        )

    def test_get_user_profile_page(self):
        """ get user profile page as logged in user """
        self.client.login(username="bobby", password="temporary")
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_get_user_profile_404(self):
        """ return 404 if url incorrect """
        response = self.client.get("/profile/fewt")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_unregistered_attempt_to_get_profile(self):
        """ redirect from profile if user not logged in """
        response = self.client.get("/profile/", follow=True)
        self.assertRedirects(response, "/accounts/login/?next=%2Fprofile%2F")
        self.assertTemplateUsed(response, "account/login.html")

    def test_update_user_profile(self):
        """ updates the userprofile """
        self.client.login(username="bobby", password="temporary")
        data = {"default_phone_number": "12345"}
        response = self.client.post("/profile/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        # successful update
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("Profile updated successfully!" in message.message)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_invalid_update_user_profile(self):
        """ invalid updates the userprofile """
        self.client.login(username="bobby", password="temporary")
        data = {
            "default_phone_number": "12345444444535839045890"
        }
        response = self.client.post("/profile/", data, follow=True)
        self.assertEqual(response.status_code, 200)
        # invalid form update
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Update failed. Please insure the form information is valid."
            in message.message
        )
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_order_history_view(self):
        """ creates an order and checks it can be accesed in the history """
        self.client.login(username="bobby", password="temporary")
        temp_profile = UserProfile.objects.get(user__username="bobby")
        temp_order = Order.objects.create(
            full_name="bobby jones",
            user_profile=temp_profile,
            email="temporary@gmail.com",
            phone_number="122345",
            country="US",
            postcode="rsds234",
            town_or_city="hometown",
            street_address1="1 hosest",
            street_address2="2 street",
            county="yes",
            stripe_pid="random_id",
            original_cart="2,4,5",
        )

        response = self.client.get(
            f"/profile/order_history/{temp_order.order_number}", follow=True
        )
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "info")
        self.assertTrue(
            f"This is a past confirmation for order number "
            f"{temp_order.order_number}."
            in message.message
        )
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
