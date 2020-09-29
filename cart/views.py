from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from games.models import Game


def view_cart(request):
    """ renders a view to see the games in the shopping cart """
    return render(request, "cart/cart.html")


def add_to_cart(request, game_id):
    """
    Adds a game to the shopping cart using the game_id
     passed from the games detail page
    """
    try:
        game = get_object_or_404(Game, pk=game_id)

        # get the cart list from the session or create one
        cart = request.session.get("cart", [])

        # only add a game to the cart if it is not in the cart already
        if game_id not in cart:
            cart.append(game_id)
            # Success message
            messages.success(request, f"Added {game.name} to your cart!")
        else:
            # Error message
            messages.error(request, f"{game.name} is already in your cart!")

        # update the session list
        request.session["cart"] = cart

    except Exception as e:
        messages.error(request, f"Error adding item: {e}")
        return redirect("/cart/")

    return redirect("/cart/")


def remove_from_cart(request, game_id):
    """ Removes a game from the cart using the game_id """
    try:
        # get the game if it exists
        game = get_object_or_404(Game, pk=game_id)

        cart = request.session.get("cart", [])
        # only delete a game if it is in the cart already
        if str(game_id) in cart:
            cart.remove(game_id)
            # Warning message
            messages.warning(request, f"Removed {game.name} from your cart!")
        else:
            # Error message
            messages.error(request, "Game not found in your cart!")
        # update the session list
        request.session["cart"] = cart
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect("/cart/")

    return redirect("/cart/")
