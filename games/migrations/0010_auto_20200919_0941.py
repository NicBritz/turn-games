# Generated by Django 3.1.1 on 2020-09-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_auto_20200907_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='header_image_url',
            field=models.URLField(
                blank=True,
                default='https://res.cloudinary.com/dajuujhvs/image/upload/'
                        'v1600508372/turn_games/placeholder_if4uza.jpg',
                max_length=1024, null=True),
        ),
    ]
