from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Game, Category, Genre, Tag


def all_games(request):
    """ returns the all products view  """
    query = None
    category = None
    genre = None
    tag = None
    search_term = None
    current_selection = None
    sort = None
    direction = None

    games = Game.objects.all()

    # check if the request is a get request
    if request.GET:

        # sorting and ordering
        if "sort" in request.GET:
            sort_key = request.GET["sort"]
            sort = sort_key

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sort_key = f"-{sort_key}"

            games = games.order_by(sort_key)

        # check if filtering by category
        if "category" in request.GET:
            category = request.GET["category"]

            if category == "all":
                games = Game.objects.all()
                current_selection = "All"
            else:
                games = games.filter(categories__name__iexact=category)
                current_selection = Category.objects.filter(name__iexact=category)

        # check if filtering by Genre
        if "genre" in request.GET:
            genre = request.GET["genre"]
            games = games.filter(genres__name__iexact=genre)
            current_selection = Genre.objects.filter(name__iexact=genre)

        # check if filtering by Tag
        if "tag" in request.GET:
            tag = request.GET["tag"]
            games = games.filter(tags__name__iexact=tag)
            current_selection = Tag.objects.filter(name__iexact=tag)

        # check if filtering by discount1
        if "special_offers" in request.GET:
            offer = request.GET["special_offers"]

            if offer == "discounted":
                games = games.filter(discounted=True)
                current_selection = "Discounted"

            elif offer == "featured":
                games = games.filter(featured=True)
                current_selection = "Featured"

        # check if it is a search query
        if "q" in request.GET:
            query = request.GET["q"]
            # If the user has not entered any text display an error
            if not query:
                messages.error(request, "No search text entered!")
                return redirect(reverse("games"))

            # filter search based on name or description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            games = games.filter(queries)

    sorting = f"{sort}_{direction}"

    context = {
        "games": games,
        "search_term": query,
        "current_selection": current_selection,
        "sorting": sorting,
    }
    return render(request, "games/games.html", context)


def game_detail(request, game_id):
    """ returns the game detail view with all the games information """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        "game": game,
    }
    return render(request, "games/game_detail.html", context)
