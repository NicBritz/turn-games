from django.db import models
import datetime


# Category Model
class Category(models.Model):
    # clean up group name in Django admin area
    class Meta:
        verbose_name_plural = "Categories"

    """ This model handles all the fields for a game category"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Genre Model
class Genre(models.Model):
    """ This model handles all the fields for a game genre """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Tags Model
class Tag(models.Model):
    """ This model handles all the fields for a game tag """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Games Model
class Game(models.Model):
    """ This model handles all the fields for a game entry """

    name = models.CharField(max_length=254)
    description = models.TextField()
    header_image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        default="https://res.cloudinary.com/dajuujhvs/image/upload/v1600508372/turn_games/placeholder_if4uza.jpg",
    )
    release_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    developer = models.CharField(max_length=254, null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    platforms = models.CharField(max_length=254, null=True, blank=True)
    positive_ratings = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True, default=0
    )
    negative_ratings = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True, default=0
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price_discounted = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    featured = models.BooleanField(default=False)
    discounted = models.BooleanField(default=False)
    discount_percent = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, default=0
    )
    categories = models.ManyToManyField(Category, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
