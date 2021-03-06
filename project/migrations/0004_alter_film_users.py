# Generated by Django 4.0.3 on 2022-04-15 11:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_film_options_userfilms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='users',
        ),
        migrations.AddField(
            model_name='film',
            name='users',
            field=models.ManyToManyField(related_name='films', through='project.UserFilms', to=settings.AUTH_USER_MODEL),
        ),
    ]
