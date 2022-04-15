# Generated by Django 4.0.3 on 2022-04-15 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_film'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.CreateModel(
            name='UserFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]