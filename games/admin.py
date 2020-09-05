from django.contrib import admin

from .models import Game, Category, Genre, Tag


# clean up Game admin in django admin area
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'developer',
        'publisher',
        'price'
    )


# clean up Category admin in django admin area
class CategoryAdmin(admin.ModelAdmin):
    pass


# clean up Genre admin in django admin area
class GenreAdmin(admin.ModelAdmin):
    pass


# clean up Tag admin in django admin area
class TagAdmin(admin.ModelAdmin):
    pass


# Register the application models
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Tag)
