# Generated by Django 5.1 on 2024-08-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_app', '0003_alter_profile_age_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(choices=[('All', 'All'), ('Kids', 'Kids'), ('Adults', 'Adults')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('All', 'All'), ('Kids', 'Kids'), ('Adults', 'Adults')], max_length=20),
        ),
    ]
