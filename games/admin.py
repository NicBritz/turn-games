from django.contrib import admin

from .models import Game, Category, Genre, Tags

# Register the application models
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Tags)
