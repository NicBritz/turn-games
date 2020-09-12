from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ Adds a checkout view """
    cart = request.session.get("cart", {})

    # if the cart is empty
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse("games"))

    order_form = OrderForm()
    template = "checkout/checkout.html"

    context = {
        "order_form": order_form,
        'stripe_public_key': "pk_test_51H80TcHt6cR2AbTyFtNNcSQYlDJpVpiLk9t5eprBzoYzbuqAGpQILKKgfhW4DcAnEQ9cIItEDr8324eUGBmWt0BD00Rsnp2SRs",
        'client_secret': "test client secret",
    }

    return render(request, template, context)


def payment(request):
    """ renders a view to enter your payment information """
    context = {
        'stripe_public_key': "pk_test_51H80TcHt6cR2AbTyFtNNcSQYlDJpVpiLk9t5eprBzoYzbuqAGpQILKKgfhW4DcAnEQ9cIItEDr8324eUGBmWt0BD00Rsnp2SRs",
        'client_secret': "test client secret",
    }
    return render(request, "checkout/payment.html", context)
