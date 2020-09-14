from django import forms
from games.models import Game, Category, Genre, Tag


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # make category list friendly names
        categories = Category.objects.all()
        categories_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields["categories"].choices = categories_friendly_names

        # make genre list friendly names
        genres = Genre.objects.all()
        genres_friendly_names = [(g.id, g.get_friendly_name()) for g in genres]
        self.fields["genres"].choices = genres_friendly_names

        # make genre list friendly names
        tags = Tag.objects.all()
        tags_friendly_names = [(t.id, t.get_friendly_name()) for t in tags]
        self.fields["tags"].choices = tags_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input"
