from django.shortcuts import render, redirect


def view_cart(request):
    """ view the items in the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, game_id):
    """ Adds a game to the cart """
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart',[])

    if game_id not in cart:
        cart.append(game_id)

    request.session['cart'] = cart

    return redirect(redirect_url)
