# Generated by Django 4.2.2 on 2023-06-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0039_upload_useremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='marriage_photos',
            field=models.TextField(null=True),
        ),
    ]
