# Generated by Django 4.2.1 on 2023-05-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0022_profile_finder_aadharo_profile_finder_addresso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_finder',
            name='dobo',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='father_nameo',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
