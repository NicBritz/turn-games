# Generated by Django 3.1.1 on 2020-09-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0019_game_price_calculated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='price_calculated',
        ),
    ]