from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import OrderForm
from django.conf import settings


def checkout(request):
    """ Adds a checkout view """
    cart = request.session.get("cart", {})

    # if the cart is empty
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse("games"))

    order_form = OrderForm()
    template = "checkout/checkout.html"

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": stripe_secret_key,
    }

    return render(request, template, context)
