from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add initial settings
        """
        super().__init__(*args, **kwargs)

        # Make the phone number autofocused
        self.fields["default_phone_number"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if field == "default_country":
                # country field has select class
                self.fields[field].widget.attrs["class"] = " "
            else:
                # all other fields have input class
                self.fields[field].widget.attrs["class"] = "input"
