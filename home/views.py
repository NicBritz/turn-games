from django.shortcuts import render
from games.models import Game
from django.db.models import Q


def index(request):
    """
    Renders the home page passing in all the products
    """

    # get all games in the database
    games = Game.objects.all()
    # filter the specials and featured
    featured_specials = games.filter(Q(discounted=True) | Q(featured=True))


    context = {"featured_specials": featured_specials}
    url = "home/index.html"

    return render(request, url, context)
