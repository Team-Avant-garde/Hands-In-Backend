# Generated by Django 4.2.7 on 2023-11-07 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('content', models.CharField(max_length=4000)),
                ('tag', models.CharField(db_index=True, max_length=50)),
                ('is_solved', models.BooleanField(default=False)),
                ('post_image', models.CharField(blank=True, max_length=255)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]