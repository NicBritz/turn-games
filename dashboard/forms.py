from django import forms
from games.models import Game, Category, Genre, Tag


class GameForm(forms.ModelForm):
    category_multi = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)

    genre_multi = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)

    tag_multi = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)

    class Meta:
        model = Game
        fields = ('name', 'header_image_url', 'header_image', 'release_date',
                  'developer', 'publisher', 'platforms', 'price',
                  'discount_percent', 'categories', 'genres','featured', 'discounted',
                  'tags', 'description', 'header_image', 'category_multi',
                  'genre_multi', 'tag_multi')

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

        # Make the fullname autofocused
        self.fields["name"].widget.attrs["autofocus"] = True

        inputs = ['name', 'header_image_url', 'header_image', 'release_date',
                  'developer', 'publisher', 'platforms', 'price', 'discount_percent']
        multiples = ['categories', 'genres', 'tags']
        checkboxes = ['featured', 'discounted', ]
        text_areas = ['description']
        file_inputs = ['header_image']

        for field_name, field in self.fields.items():
            if field_name in inputs:
                field.widget.attrs["class"] = "input"

            if field_name in text_areas:
                field.widget.attrs["class"] = "textarea"

            if field_name in file_inputs:
                field.widget.attrs["class"] = "file-input"

            if field_name in checkboxes:
                field.widget.attrs["class"] = "checkbox"

            if field_name in multiples:
                field.widget.attrs["multiple"] = True
                field.widget.attrs["size"] = 6

            if field_name in 'category_multi':
                field.choices = categories_friendly_names

            if field_name in 'genre_multi':
                field.choices = genres_friendly_names

            if field_name in 'tag_multi':
                field.choices = tags_friendly_names

