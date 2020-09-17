from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add_game/', views.add_game, name="add_game"),
]
