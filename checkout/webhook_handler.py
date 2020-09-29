from django.http import HttpResponse
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from games.models import Game
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
import time
import json


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        private method to send a confirmation email to the customer
        """
        customer_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_subject.txt", {"order": order}
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])

    def handle_event(self, event):
        """
        Handle a generic or unknown webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        intent_id = intent.id
        cart = intent.metadata.cart
        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Get the userprofile
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    grand_total=grand_total, stripe_pid=intent_id, original_cart=cart,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # send confirmation email
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    stripe_pid=intent_id,
                    original_cart=cart,
                )
                # create the line items for the order from the cart contents
                for current_game in json.loads(cart):
                    # get the game record
                    game = Game.objects.get(id=current_game)
                    # add a record to the line items
                    order_line_item = OrderLineItem(order=order, game=game,)
                    # save the record
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f'webhook received: {event["type"]}', status=200)
