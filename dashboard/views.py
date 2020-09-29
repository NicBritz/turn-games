from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import User
from checkout.models import Order
from games.models import Game
from .forms import GameForm
from django.contrib.admin.models import LogEntry
from decimal import Decimal
from django.db.models import Q, Sum
from datetime import timedelta
from django.utils import timezone


@login_required
def dashboard(request):
    """
   renders the main admin dashboard
    """

    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin users can do that.")
        return redirect(reverse("home"))

    # log entry src https://stackoverflow.com/questions/5746624/showing-django-admin-actions-on-template
    logs = LogEntry.objects.select_related().all().order_by("-id")[:10]

    all_games = Game.objects.all()
    all_users = User.objects.all()
    all_orders = Order.objects.all()
    orders_per_month = []

    last_month = timezone.now() - timedelta(days=30)
    # calculate the number of orders per day
    orders_per_day = (
        all_orders.filter(date__gt=last_month)
        .extra(select={"day": "date(date)"})
        .values("day")
        .annotate(sum=Sum("grand_total"))
    )

    for day in orders_per_day:
        orders_per_month.append(float(day["sum"]))

    total_sales = Decimal(0)
    for order in all_orders:
        total_sales += order.grand_total

    context = {
        "logs": logs,
        "all_games": all_games,
        "all_orders": all_orders,
        "total_sales": total_sales,
        "all_users": all_users,
        "orders_per_month": orders_per_month,
    }

    return render(request, "dashboard/dashboard.html", context)


@login_required
def add_game(request):
    """
    Renders a view to add a product to the database
    """
    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        # add a game using the game form data
        game_form = GameForm(request.POST)
        if game_form.is_valid():
            game = game_form.save()
            messages.success(request, "Successfully added the Game!")
            return redirect(reverse("game_detail", args=[game.id]))
        else:
            messages.error(
                request, "Failed to add the Game. Please ensure the form is valid!"
            )
    else:
        game_form = GameForm()

    context = {
        "game_form": game_form,
    }
    return render(request, "dashboard/add_game.html", context)


@login_required
def edit_game(request, game_id):
    """ Edit game in database """

    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    game = get_object_or_404(Game, pk=game_id)

    if request.method == "POST":
        # edit a game using the form data
        game_form = GameForm(request.POST, request.FILES, instance=game)
        if game_form.is_valid():
            game = game_form.save()
            messages.success(request, f"Successfully updated {game.name}!")
            return redirect(reverse("game_detail", args=[game.id]))
        else:
            messages.error(
                request, "Failed to update the Game. Please ensure the form is valid!"
            )
    else:
        game_form = GameForm(instance=game)
        messages.info(request, f"you are now editing {game.name}!")

    template = "dashboard/edit_game.html"
    context = {
        "game_form": game_form,
        "game": game,
    }

    return render(request, template, context)


@login_required
def delete_game(request, game_id):
    """ Delete game in database """

    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, "Game deleted!")
    return redirect(reverse("games_management"))


@login_required
def games_management(request):
    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    """ Game management view """
    all_games = Game.objects.all()
    all_users = User.objects.all()
    all_orders = Order.objects.all()
    all_games = all_games.order_by("name")
    filtered_games = all_games.order_by("name")
    search_term = None

    total_sales = Decimal(0)
    for order in all_orders:
        total_sales += order.grand_total

    # check if it is a search query
    if "q" in request.GET:
        query = request.GET["q"]
        search_term = query
        # If the user has not entered any text display an error
        if not query:
            messages.error(request, "No search text entered!")
            return redirect(reverse("games_management"))

        # filter search based on name
        filtered_games = all_games.filter(Q(name__icontains=query))

    context = {
        "all_games": all_games,
        "all_users": all_users,
        "all_orders": all_orders,
        "total_sales": total_sales,
        "filtered_games": filtered_games,
        "search_term": search_term,
    }

    return render(request, "dashboard/games_management.html", context)


@login_required
def user_management(request):
    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    """ User management view """
    all_games = Game.objects.all()
    all_users = User.objects.all()
    all_orders = Order.objects.all()
    filtered_users = all_users.order_by("username")
    search_term = None

    total_sales = Decimal(0)
    for order in all_orders:
        total_sales += order.grand_total

    # check if it is a search query
    if "q" in request.GET:
        query = request.GET["q"]
        search_term = query
        # If the user has not entered any text display an error
        if not query:
            messages.error(request, "No search text entered!")
            return redirect(reverse("user_management"))

        # filter search based on name
        filtered_users = all_users.filter(Q(username__icontains=query))

    context = {
        "all_games": all_games,
        "all_users": all_users,
        "all_orders": all_orders,
        "total_sales": total_sales,
        "filtered_users": filtered_users,
        "search_term": search_term,
    }

    return render(request, "dashboard/user_management.html", context)


@login_required
def delete_user(request, user_id):
    """ Delete game in database """

    user = get_object_or_404(User, pk=user_id)

    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    user.delete()
    messages.success(request, "User deleted!")
    return redirect(reverse("user_management"))


@login_required
def order_management(request):
    """ User management view """
    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    all_games = Game.objects.all()
    all_users = User.objects.all()
    all_orders = Order.objects.all()
    filtered_orders = all_orders.order_by("-date")
    search_term = None

    total_sales = Decimal(0)
    for order in all_orders:
        total_sales += order.grand_total

    # check if it is a search query
    if "q" in request.GET:
        query = request.GET["q"]
        search_term = query
        # If the user has not entered any text display an error
        if not query:
            messages.error(request, "No search text entered!")
            return redirect(reverse("user_management"))

        # filter search based on name
        filtered_orders = all_orders.filter(Q(order_number__icontains=query))

    context = {
        "all_games": all_games,
        "all_users": all_users,
        "all_orders": all_orders,
        "total_sales": total_sales,
        "filtered_orders": filtered_orders,
        "search_term": search_term,
    }

    return render(request, "dashboard/order_management.html", context)


@login_required
def order_view(request, order_number):
    """ render the success view """

    # redirect to home if not superuser
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admin uses can do that.")
        return redirect(reverse("home"))

    order = get_object_or_404(Order, order_number=order_number)
    order_tax = order.grand_total - order.order_total

    context = {"order": order, "order_tax": order_tax}

    return render(request, "dashboard/order_view.html", context)
