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
    )

    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "phone_number",
        "order_total",
        "grand_total",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
