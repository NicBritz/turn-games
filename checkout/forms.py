from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "county",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Add initial settings
        """
        super().__init__(*args, **kwargs)

        # Make the fullname autofocused
        self.fields["full_name"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if field == "country":
                # country field has select class
                self.fields[field].widget.attrs["class"] = " "
            else:
                # all other fields have input class
                self.fields[field].widget.attrs["class"] = "input"
