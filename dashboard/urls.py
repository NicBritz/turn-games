from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('games_management/', views.games_management, name="games_management"),
    path('add_game/', views.add_game, name="add_game"),
    path('edit_game/<int:game_id>/', views.edit_game, name="edit_game"),
    path('delete_game/<int:game_id>/', views.delete_game, name="delete_game"),
]
