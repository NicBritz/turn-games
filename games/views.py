from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Game, Category, Genre, Tag


def all_games(request):
    """ returns the all games view filter dependant """

    query = None
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
            # factor in discounts when sorting
            if sort == "price":
                sort_key = "price_discounted"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sort_key = f"-{sort_key}"
            # order the games according to the selection
            games = games.order_by(sort_key)

        # check if filtering by category
        if "category" in request.GET:
            category = request.GET["category"]

            if category == "all":
                current_selection = "All"
            else:
                games = games.filter(categories__name__iexact=category)
                current_selection = Category.objects.filter(
                    name__iexact=category)

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

        # check if filtering by discount
        if "special_offers" in request.GET:
            offer = request.GET["special_offers"]

            if offer == "discounted":
                games = games.filter(discounted=True)
                current_selection = "Discounted"

            elif offer == "featured":
                games = games.filter(featured=True)
                current_selection = "Featured"

            elif offer == "free":
                games = games.filter(price=0)
                current_selection = "Free"

        # check if it is a search query
        if "q" in request.GET:
            query = request.GET["q"]
            # If the user has not entered any text display an error
            if not query:
                messages.error(request, "No search text entered!")
                return redirect(reverse("games"))

            # filter search based on name or description
            ques = Q(name__icontains=query) | Q(description__icontains=query)
            games = games.filter(ques)

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


def rate_game(request, game_id, rating):
    """ Adds a rating to a game as long as the user is logged in """

    game = get_object_or_404(Game, pk=game_id)

    if request.user.is_authenticated:
        if rating == "1":
            game.positive_ratings += 1
            messages.success(request, "Added a positive rating!")
            game.save()
        elif rating == "0":
            game.negative_ratings += 1
            messages.success(request, "Added a negative rating!")
            game.save()
        else:
            messages.error(request, "No ratings changed!")
            return redirect(reverse("games"))
    else:
        messages.error(request, "You must be logged in to rate this game!")

    return redirect("game_detail", game_id)
