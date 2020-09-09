from django.shortcuts import render


def view_cart(request):
    """ view the items in the shopping cart """
    return render(request, 'cart/cart.html')