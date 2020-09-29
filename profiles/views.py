from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile page
    """
    # get the users profile
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        # update the users profile
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
        else:
            messages.error(
                request, "Update failed. Please insure the form information is valid."
            )
    else:
        # add users data to the profile form
        profile_form = UserProfileForm(instance=user_profile)

    # find all previous orders
    previous_orders = user_profile.orders.all().order_by("-date")

    context = {"profile_form": profile_form, "previous_orders": previous_orders}

    return render(request, "profiles/profile.html", context)


@login_required
def order_history(request, order_number):
    """
        display a previously successful order
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request, f"This is a past confirmation for order number {order_number}."
    )

    template = "checkout/checkout_success.html"

    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
