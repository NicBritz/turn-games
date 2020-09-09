from django.shortcuts import render, redirect
from django.contrib import messages

from games.models import Game

def view_cart(request):
    """ view the items in the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, game_id):
    """ Adds a game to the cart """
    game = Game.objects.get(pk=game_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', [])

    if game_id not in cart:
        cart.append(game_id)

    request.session['cart'] = cart
    messages.info(request, f'Added {game.name} to your cart')

    return redirect(redirect_url)


def remove_from_cart(request, game_id):
    """ Removes a game from the cart """

    cart = request.session.get('cart', [])

    if str(game_id) in cart:
        cart.remove(game_id)

    request.session['cart'] = cart

    return redirect('/cart/')
