# Generated by Django 4.2.7 on 2023-11-09 10:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]