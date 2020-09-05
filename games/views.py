from django.shortcuts import render
from .models import Game


def all_games(request):
    """ returns the all products view - it also handles teh sorting ands searching functionality """

    games = Game.objects.all()

    context = {
        'games': games,
    }
    return render(request, 'games/games.html', context)
