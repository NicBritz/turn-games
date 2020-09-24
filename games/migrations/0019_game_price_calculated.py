# Generated by Django 3.1.1 on 2020-09-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0018_remove_game_discounted_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price_calculated',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]