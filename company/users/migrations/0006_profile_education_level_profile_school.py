# Generated by Django 5.1.7 on 2025-05-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_educationlevel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education_level',
            field=models.CharField(choices=[('secondary', 'Secondary'), ('undergraduate', 'Undergraduate'), ('tertiary', 'Tertiary Instituition'), ('postgraduate', 'Postgraduate')], default='', max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(default='', max_length=250),
        ),
    ]
