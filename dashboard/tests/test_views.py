from django.test import TestCase
from games.models import Game
from checkout.models import Order, OrderLineItem
from profiles.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


class TestDashboardViews(TestCase):
    """ Tests for dashboard Views """

    def setUp(self):
        user_model = get_user_model()
        standard_user = user_model.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )
        super_user = user_model.objects.create_superuser(
            "admin", "admin@gmail.com", "admin"
        )

    def test_unauthorised_get_dashboard_page(self):
        """ un-authorised user attempt dashboard """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/", follow=True)
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("Sorry, only admin users can do that." in message.message)
        self.assertRedirects(response, "/")

    def test_authorised_get_dashboard_page(self):
        """ authorised user access dashboard """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/",)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

    def test_unauthorised_get_add_game_page(self):
        """ un-authorised user attempt add game """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/add_game/", follow=True)
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertRedirects(response, "/")

    def test_authorised_get_add_game_page(self):
        """ authorised user access add game """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/add_game/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/add_game.html")

    def test_add_game_from_view(self):
        """ add a game to the database through the add game view"""
        self.client.login(username="admin", password="admin")
        data = {"name": "test", "description": "test game", "price": "5.00"}
        response = self.client.post("/dashboard/add_game/", data=data)
        temp_game = get_object_or_404(Game, pk=1)
        self.assertRedirects(response, f"/games/{temp_game.id}/")

    def test_edit_game_from_view(self):
        """ edit a game in the database through the edit game view """
        self.client.login(username="admin", password="admin")
        data = {"name": "test", "description": "test game", "price": "5.00"}
        self.client.post("/dashboard/add_game/", data=data)
        temp_game = get_object_or_404(Game, pk=1)
        new_data = {"name": "new_test"}
        response = self.client.post(
            f"/dashboard/edit_game/{temp_game.id}/", data=new_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        self.assertTemplateUsed(response, "dashboard/edit_game.html")

    def test_delete_game_from_view(self):
        """ authorised game delete from view """
        self.client.login(username="admin", password="admin")
        data = {"name": "test", "description": "test game", "price": "5.00"}
        self.client.post("/dashboard/add_game/", data=data)
        games = Game.objects.all()
        self.assertEqual(len(games), 1)
        response = self.client.get("/dashboard/delete_game/1", follow=True)
        self.assertEqual(response.status_code, 200)
        updated_games = Game.objects.all()
        self.assertEqual(len(updated_games), 0)
        self.assertTemplateUsed(response, "dashboard/games_management.html")

    def test_authorised_get_games_management_page(self):
        """ authorised user access games management """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/games_management", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/games_management.html")

    def test_unauthorised_get_games_management_page(self):
        """ un-authorised user attempt games management """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/games_management/", follow=True)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertRedirects(response, "/")

    def test_authorised_get_user_management_page(self):
        """ authorised user access user management """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/user_management", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/user_management.html")

    def test_unauthorised_get_user_management_page(self):
        """ un-authorised user attempt user management """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/user_management/", follow=True)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertRedirects(response, "/")

    def test_delete_user_from_view(self):
        """ authorised user delete """
        self.client.login(username="admin", password="admin")
        users = User.objects.all()
        self.assertEqual(len(users), 2)
        response = self.client.get("/dashboard/delete_user/1", follow=True)
        self.assertEqual(response.status_code, 200)
        updated_users = User.objects.all()
        self.assertEqual(len(updated_users), 1)
        self.assertTemplateUsed(response, "dashboard/user_management.html")

    def test_authorised_get_order_management_page(self):
        """ authorised user access order management """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/order_management", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/order_management.html")

    def test_unauthorised_get_order_management_page(self):
        """ un-authorised user attempt order management """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/order_management/", follow=True)
        # get message from context and check that expected text is there
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertRedirects(response, "/")

    def test_get_order_view(self):
        """ see previous order view """
        self.client.login(username="admin", password="admin")
        temp_game = Game.objects.create(
            name="test_game", description="test_description",
        )
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
            f"/dashboard/order_view/{temp_order.order_number}", follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/order_view.html")
