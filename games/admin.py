from django.contrib import admin

from .models import Game, Category, Genre, Tag


# clean up Game admin in django admin area
class GameAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "developer", "publisher", "price", "featured")
    ordering = ("name",)


# clean up Category admin in django admin area
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("friendly_name", "name")

    ordering = ("name",)


# clean up Genre admin in django admin area
class GenreAdmin(admin.ModelAdmin):
    list_display = ("friendly_name", "name")

    ordering = ("name",)


# clean up Tag admin in django admin area
class TagAdmin(admin.ModelAdmin):
    list_display = ("friendly_name", "name")

    ordering = ("name",)


# Register the application models
admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Tag, TagAdmin)
