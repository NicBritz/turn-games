from . import views
from django.urls import path

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("games_management/", views.games_management, name="games_management"),
    path("user_management/", views.user_management, name="user_management"),
    path("order_management/", views.order_management, name="order_management"),
    path("add_game/", views.add_game, name="add_game"),
    path("edit_game/<int:game_id>/", views.edit_game, name="edit_game"),
    path("delete_game/<int:game_id>/", views.delete_game, name="delete_game"),
    path("delete_user/<int:user_id>/", views.delete_user, name="delete_user"),
    path("order_view/<order_number>", views.order_view, name="order_view"),
]
