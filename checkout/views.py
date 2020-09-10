from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get("cart", {})

    # if the cart is empty
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse("games"))

    order_form = OrderForm()
    template = "checkout/checkout.html"

    context = {
        "order_form": order_form,
    }

    return render(request, template, context)
