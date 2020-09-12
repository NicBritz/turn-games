from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from games.models import Game


def cart_contents(request):
    """ bag contents context processor to keep track of bag items """
    cart = request.session.get("cart", [])
    cart_items = []
    total = 0

    # iterate through the items in the cart
    for item in cart:
        # get the database record
        game = get_object_or_404(Game, pk=item)
        # calculate the discount
        discount = game.price * (game.discount_percent / Decimal(100))
        # calculate the discounted price
        discounted_price = game.price - discount
        # add the price to the total
        total += discounted_price

        # append the values to the cart items list
        cart_items.append(
            {"game_id": game.id, "game_discount_price": discounted_price, "game": game, }
        )
    # calculate the tax
    tax = total * Decimal(settings.TAX_PERCENTAGE)
    # calculate the grand total
    grand_total = total + tax

    context = {
        "cart_items": cart_items,
        "total": total,
        "tax": tax,
        "grand_total": grand_total,
    }

    return context
