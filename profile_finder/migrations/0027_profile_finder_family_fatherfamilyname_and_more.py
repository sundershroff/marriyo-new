# Generated by Django 4.2.1 on 2023-05-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0026_profile_finder_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_finder',
            name='family_fatherfamilyname',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='family_motherfamilyname',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
