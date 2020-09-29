from django.test import TestCase
from games.models import Game
from checkout.models import Order, OrderLineItem
from profiles.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


class TestDashboardViews(TestCase):
    """ Tests for dashboard Views """

    def setUp(self):
        """ setup users """
        user_model = get_user_model()
        user_model.objects.create_user(
            "temporary",
            "temporary@gmail.com",
            "temporary"
        )
        user_model.objects.create_superuser(
            "admin",
            "admin@gmail.com",
            "admin"
        )

    def test_un_authorised_get_dashboard_page(self):
        """ un-authorised user attempt to view dashboard """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/", follow=True)
        self.assertEqual(response.status_code, 200)
        # error message: only admin can do that
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Sorry, only admin users can do that." in message.message)
        self.assertRedirects(response, "/")

    def test_authorised_get_dashboard_page(self):
        """ authorised user access dashboard """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/", )
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
        # invalid form
        err_response = self.client.post("/dashboard/add_game/", data={})
        message = list(err_response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Failed to add the Game. Please ensure the form is valid!"
            in message.message
        )

    def test_edit_game_from_view(self):
        """ edit a game in the database through the edit game view """
        self.client.login(username="admin", password="admin")
        Game.objects.create(name="test", description="test_game")
        temp_game = get_object_or_404(Game, pk=1)
        new_data = {
            "name": "test",
            "description": "test data",
            "price": "10.00",
        }
        get_response = self.client.get(f"/dashboard/edit_game/{temp_game.id}/")
        message = list(get_response.context.get("messages"))[0]
        # success edit game - you are now editing test
        self.assertEqual(message.tags, "info")
        response = self.client.post(
            f"/dashboard/edit_game/{temp_game.id}/", data=new_data, follow=True
        )
        self.assertEqual(response.status_code, 200)

        # successful update
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "success")
        # redirect to game details
        self.assertTemplateUsed(response, "games/game_detail.html")

    def test_edit_game_invalid_form(self):
        """
        edit a game in the database
        through the edit game view invalid form
        """
        self.client.login(username="admin", password="admin")
        Game.objects.create(name="test", description="test_game")
        temp_game = get_object_or_404(Game, pk=1)
        new_data = {
            "name": "",
            "description": "test data",
            "price": "10.00",
        }
        response = self.client.post(
            f"/dashboard/edit_game/{temp_game.id}/", data=new_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        message = list(response.context.get("messages"))[0]
        # invalid to update game - invalid form
        self.assertEqual(message.tags, "error")
        # redirect to game details
        self.assertTemplateUsed(response, "dashboard/edit_game.html")

    def test_un_authorised_edit_game_from_view(self):
        """
        attempt edit a game in the database
        through the edit game view non admin user
        """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/edit_game/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        # error message - only admin users can do that
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTemplateUsed(response, "home/index.html")

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

    def test_un_authorised_delete_game_from_view(self):
        """ un authorised game delete from view """
        self.client.login(username="temporary", password="temporary")
        Game.objects.create(name="test", description="test_game")
        response = self.client.post("/dashboard/delete_game/1", follow=True)
        # message only admin can do this
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_authorised_get_games_management_page(self):
        """ authorised user access games management """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/games_management", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/games_management.html")

    def test_authorised_get_games_management_page_search(self):
        """ authorised user access games management """
        self.client.login(username="admin", password="admin")
        # invalid search
        response = self.client.get(
            "/dashboard/games_management/?q",
            follow=True)
        message = list(response.context.get("messages"))[0]
        # no search text entered message
        self.assertEqual(message.tags, "error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/games_management.html")

    def test_unauthorised_get_games_management_page(self):
        """ un-authorised user attempt games management """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/games_management/", follow=True)
        # only admin users can do that
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertRedirects(response, "/")

    def test_authorised_get_user_management_page(self):
        """ authorised user access user management """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/user_management", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/user_management.html")

    def test_authorised_get_user_management_page_search(self):
        """ authorised user access user management """
        self.client.login(username="admin", password="admin")
        # invalid search
        response = self.client.get(
            "/dashboard/user_management/?q",
            follow=True)
        message = list(response.context.get("messages"))[0]
        # no search text entered message
        self.assertEqual(message.tags, "error")
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

    def test_un_authorised_delete_user_from_view(self):
        """ see previous order view """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/delete_user/1", follow=True)
        self.assertEqual(response.status_code, 200)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTemplateUsed(response, "home/index.html")

    def test_authorised_get_order_management_page(self):
        """ authorised user access order management """
        self.client.login(username="admin", password="admin")
        response = self.client.get("/dashboard/order_management", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/order_management.html")

    def test_authorised_get_order_management_page_search(self):
        """ authorised user access order management """
        self.client.login(username="admin", password="admin")
        # invalid search
        response = self.client.get(
            "/dashboard/order_management/?q",
            follow=True)
        message = list(response.context.get("messages"))[0]
        # no search text entered message
        self.assertEqual(message.tags, "error")
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

    def test_un_authorised_get_order_view(self):
        """ see previous order view """
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/dashboard/order_view/1", follow=True)
        self.assertEqual(response.status_code, 200)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(message.tags, "error")
        self.assertTemplateUsed(response, "home/index.html")
