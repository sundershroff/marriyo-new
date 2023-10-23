# Generated by Django 4.1.6 on 2023-05-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_finder', '0017_profile_finder_contact_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_finder',
            name='Course',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='Course1',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='Why_marry',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='are_you_disable',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='are_you_working_non',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='behind_the_decision',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='carrying_marriage',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='company_name',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='complexion',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='consume_alcohol',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='criminal_offences',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='family',
            field=models.FileField(blank=True, default=None, max_length=500, null=True, upload_to='Family'),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='food_taste',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='fullsize_img',
            field=models.FileField(blank=True, default=None, max_length=500, null=True, upload_to='Full_size'),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='gallery',
            field=models.FileField(blank=True, default=None, max_length=500, null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='horoscope',
            field=models.FileField(blank=True, default=None, max_length=500, null=True, upload_to='horoscope'),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='illegal_drugs',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='major',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='major1',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='marital_status',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='not_interest',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='not_interest_choose',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='opinion_diet',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='orphan',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='physical_mental_status',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='position',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='primary_dob',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='primary_email',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='primary_options_country',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='primary_phone',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='profile_tag',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='salary_range',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='school',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='school1',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='school_year',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='school_year1',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='selfie',
            field=models.FileField(blank=True, default=None, max_length=500, null=True, upload_to='head_size'),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='tobacco_product',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='treet_mypartner',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='treet_their_side',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='which_organ',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='your_interest',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile_finder',
            name='your_interest_choose',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
