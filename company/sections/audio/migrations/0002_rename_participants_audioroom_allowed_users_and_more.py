# Generated by Django 5.1.7 on 2025-04-07 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audioroom',
            old_name='participants',
            new_name='allowed_users',
        ),
        migrations.RenameField(
            model_name='audioroom',
            old_name='host',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='audioroom',
            old_name='is_private',
            new_name='is_group',
        ),
    ]
