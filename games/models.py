from django.db import models


# Category Model
class Category(models.Model):

    # clean up group name in Django admin area
    class Meta:
        verbose_name_plural = 'Categories'

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
    header_image_url = models.URLField(max_length=1024, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    developer = models.CharField(max_length=254, null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    platforms = models.CharField(max_length=254, null=True, blank=True)
    required_age = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    positive_ratings = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    negative_ratings = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    categories = models.ManyToManyField(Category)
    genres = models.ManyToManyField(Genre)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
