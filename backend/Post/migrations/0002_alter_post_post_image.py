# Generated by Django 4.2.7 on 2023-11-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]