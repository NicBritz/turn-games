from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Allows adding and editing inline items from the order model"""

    model = OrderLineItem
    readonly_fields = ("line_item_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "order_total",
        "grand_total",
        "stripe_pid",
        "original_cart"
    )

    fields = (
        "order_number",
        "stripe_pid",
        "date",
        "user_profile",
        "full_name",
        "email",
        "phone_number",
        "order_total",
        "grand_total",
        "street_address1",
        "street_address2",
        "town_or_city",
        "postcode",
        "county",
        "country",
        "original_cart"
    )

    list_display = (
        "order_number",
        "stripe_pid",
        "date",
        "full_name",
        "order_total",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
