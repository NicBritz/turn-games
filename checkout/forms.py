from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
        )

    def __init__(self, *args, **kwargs):
        """
        Add initial settings
        """
        super().__init__(*args, **kwargs)

        # Make the fullname autofocused
        self.fields["full_name"].widget.attrs["autofocus"] = True

        for field in self.fields:
            # customize the form style
            self.fields[field].widget.attrs["class"] = "input"
