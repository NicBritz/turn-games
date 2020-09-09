from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add/<game_id>/', views.add_to_cart, name="add_to_cart"),
    path('remove/<game_id>/', views.remove_from_cart, name="remove_from_cart"),
]