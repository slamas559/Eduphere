# Generated by Django 5.1.7 on 2025-05-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_alter_memberanswer_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberanswer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
