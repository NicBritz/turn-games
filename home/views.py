from django.shortcuts import render
from games.models import Game
from django.db.models import Q


def handler404(request, exception):
    return render(request, "404.html", status=404)


def handler500(request):
    return render(request, "500.html", status=500)


def index(request):
    """
    Renders the games page passing in all the products
    """

    # get all games in the database
    games = Game.objects.all()
    # filter the specials and featured
    featured_specials = games.filter(Q(discounted=True) | Q(featured=True)).order_by(
        "?"
    )
    # randomly select 10 for main slider
    # SRC: https://stackoverflow.com/questions/3506678/
    # in-django-how-do-i-select-100-random-records-from-the-database/3506692
    random_slider_content = featured_specials[:10]

    context = {
        "featured_specials": featured_specials,
        "random_slider_content": random_slider_content,
    }
    url = "home/index.html"

    return render(request, url, context)
