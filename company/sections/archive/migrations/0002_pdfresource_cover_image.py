# Generated by Django 5.1.7 on 2025-04-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfresource',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='pdf_thumbnails/'),
        ),
    ]
