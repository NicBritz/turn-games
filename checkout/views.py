from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from django.conf import settings
from cart.contexts import cart_contents
from games.models import Game
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ caches the current users order """
    try:
        # get the payment intend id
        intent_id = request.POST.get("client_secret").split("_secret")[0]
        # add the api key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # update the metadata to include custom content
        stripe.PaymentIntent.modify(
            intent_id,
            metadata={
                "cart": json.dumps(request.session.get("cart", [])),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, "We were unable to process your order. Please try again later."
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ Adds a checkout view """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":

        # get the cart contents
        cart = request.session.get("cart", [])

        # get the post data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        # check if the form is valid and save
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # get the payment intend id
            intent_id = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = intent_id
            order.original_cart = json.dumps(cart)
            order.save()
            # create the line items for the order from the cart contents
            for current_game in cart:
                try:
                    # get the game record
                    game = Game.objects.get(id=current_game)
                    # add a record to the line items
                    order_line_item = OrderLineItem(order=order, game=game,)
                    # save the record
                    order_line_item.save()

                except Game.DoesNotExist:
                    # print a error if failed
                    messages.error(
                        request, "A game in your cart was not found in our database!"
                    )
                    # delete the order
                    order.delete()
                    return redirect(reverse("view_cart"))
            # Success page
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was an error with your form. \
                       Please double check your information.",
            )
    else:
        # get the cart contents
        cart = request.session.get("cart", [])

        # if the cart is empty
        if not cart:
            messages.error(request, "Your cart is currently empty")
            return redirect(reverse("games"))

        # Stripe setup
        # get the current total and convert it for stripe
        current_cart = cart_contents(request)
        total = current_cart["grand_total"]
        stripe_total = round(total * 100)
        # set stripe API key
        stripe.api_key = stripe_secret_key
        # create the payment intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, currency=settings.STRIPE_CURRENCY
        )
        # create the order form
        order_form = OrderForm()

        template = "checkout/checkout.html"

        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """ render the success view """
    order = get_object_or_404(Order, order_number=order_number)
    order_tax = order.grand_total - order.order_total

    messages.success(
        request,
        f"Order successfully processed! \
           Your order number is {order_number}. A confirmation \
           email will be sent to {order.email}.",
    )

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"
    context = {"order": order, "order_tax": order_tax}

    return render(request, template, context)
