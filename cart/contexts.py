from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    """ bag contents context processor to keep track of bag items """
    cart_items = []
    total = 0
    game_count = 0

    tax = total * Decimal(settings.TAX_PERCENTAGE)
    grand_total = total + tax

    context = {
        "cart_items": cart_items,
        "total": total,
        "game_count": game_count,
        "tax": tax,
        "grand_total": grand_total,
    }

    return context
