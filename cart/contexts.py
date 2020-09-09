from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from games.models import Game


def cart_contents(request):
    """ bag contents context processor to keep track of bag items """
    cart = request.session.get('cart', [])
    cart_items = []
    total = 0

    for item in cart:
        game = get_object_or_404(Game, pk=item)
        discount = game.price * (game.discount_percent / Decimal(100))
        discounted_price = game.price - discount
        total += discounted_price

        cart_items.append({
            'game_id': item,
            'game_discount_price': discounted_price,
            'game': game,
        })

    tax = total * Decimal(settings.TAX_PERCENTAGE)
    grand_total = total + tax

    context = {
        "cart_items": cart_items,
        "total": total,
        "tax": tax,
        "grand_total": grand_total,
    }

    return context
