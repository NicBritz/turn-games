from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


@login_required
def profile(request):
    """
    Display the user's profile
    """
    # get the users profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
        else:
            messages.error(
                request, "Update failed. Please insure the form information is valid."
            )
    else:
        # add users data to the profile form
        profile_form = UserProfileForm(instance=profile)

    # find all previous orders
    previous_orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {"profile_form": profile_form, "previous_orders": previous_orders}

    return render(request, template, context)
