# Generated by Django 5.1 on 2024-08-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_app', '0004_alter_movie_age_limit_alter_profile_age_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='netflix_app.video'),
        ),
    ]