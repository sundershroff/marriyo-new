# Generated by Django 4.1.6 on 2023-04-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0003_profile_finder_idcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_finder',
            name='idcard',
            field=models.ImageField(blank=True, default=None, max_length=500, null=True, upload_to='pictures'),
        ),
    ]
