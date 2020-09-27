from django.shortcuts import render
from games.models import Game
from django.db.models import Q


def handler404(request, exception):
    """ return a custom 404 template """
    return render(request, "404.html", status=404)


def handler500(request):
    """ return a custom 505 template """
    return render(request, "500.html", status=500)


def index(request):
    """
    Renders the home page, with featured and discounted games
    """

    # get all the games in the database
    games = Game.objects.all()

    # filter the specials and featured ordered randomly
    # SRC: https://stackoverflow.com/questions/3506678/
    # in-django-how-do-i-select-100-random-records-from-the-database/3506692
    featured_specials = games.filter(Q(discounted=True) | Q(featured=True))
    random_slider_content = featured_specials.order_by("?")[:10]

    context = {
        "featured_specials": featured_specials,
        "random_slider_content": random_slider_content,
    }

    return render(request, "home/index.html", context)
