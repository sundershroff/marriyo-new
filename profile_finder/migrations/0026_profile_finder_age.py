# Generated by Django 4.2.1 on 2023-05-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0025_profile_finder_religion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_finder',
            name='age',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
