import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings
from games.models import Game


class Order(models.Model):
    """
    A model to keep track of all orders and order details
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    # User information
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    # Order Information
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    def _generate_order_number(self):
        """
        create a random number for the order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for tax.
        """
        self.order_total = (
            self.line_items.aggregate(Sum("line_item_total"))["line_item_total__sum"]
            or 0
        )
        # calculate the tax
        tax = self.order_total * Decimal(settings.TAX_PERCENTAGE)
        # calculate the total
        self.grand_total = self.order_total + tax
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already. src: final small project CI
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ A model to keep track of all Line Items per order """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="line_items",
    )
    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE)
    line_item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        with discounted pricing.
        """
        # calculate the discount
        discount = self.game.price * (self.game.discount_percent / Decimal(100))
        # calculate the discounted price as line total
        self.line_item_total = self.game.price - discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Game ID {self.game.id} on order {self.order.order_number}"
