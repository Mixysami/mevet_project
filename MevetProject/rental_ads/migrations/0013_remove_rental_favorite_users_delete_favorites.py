# Generated by Django 4.2.1 on 2023-05-21 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental_ads', '0012_rename_favorite_favorites_rental_favorite_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='favorite_users',
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
