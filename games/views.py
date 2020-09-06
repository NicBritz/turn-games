from django.shortcuts import render, get_object_or_404
from .models import Game, Category


def all_games(request):
    """ returns the all products view  """

    games = Game.objects.all()

    context = {
        'games': games,
    }
    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ returns the game detail view with all the games information """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }
    return render(request, 'games/game_detail.html', context)
