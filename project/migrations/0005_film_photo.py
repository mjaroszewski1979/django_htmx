# Generated by Django 4.0.3 on 2022-04-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_film_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='film_photos/'),
        ),
    ]
