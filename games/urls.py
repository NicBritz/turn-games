from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_games, name="games"),
    path('<game_id>', views.game_detail, name="game_detail"),
]
