# Generated by Django 4.2 on 2023-05-08 21:28

from django.db import migrations, models
import rental_ads.models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_ads', '0005_merge_0003_contact_0004_auto_20230507_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=rental_ads.models.rental_main_image_upload_path),
        ),
    ]