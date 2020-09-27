from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_games, name="games"),
    path('<game_id>/', views.game_detail, name="game_detail"),
    path('rate_game/<game_id>/<rating>/', views.rate_game, name="rate_game"),
]
