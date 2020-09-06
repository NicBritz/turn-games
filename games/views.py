from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Game, Category


def all_games(request):
    """ returns the all products view  """
    query = None

    games = Game.objects.all()

    # check if the request is a get request
    if request.GET:

        # check if it is a search query
        if "q" in request.GET:
            query = request.GET["q"]
            # If the user has not entered any text display an error
            if not query:
                messages.error(request, "No search text entered!")
                return redirect(reverse("games"))

            # filter search based on mame or description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            games = games.filter(queries)

    context = {
        "games": games,
        "search_term": query,
    }
    return render(request, "games/games.html", context)


def game_detail(request, game_id):
    """ returns the game detail view with all the games information """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        "game": game,
    }
    return render(request, "games/game_detail.html", context)
