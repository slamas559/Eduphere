# Generated by Django 5.1.7 on 2025-04-11 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_message_room_name_groupmessage'),
        ('groups', '0002_rename_groups_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmessage',
            name='room_name',
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
        ),
    ]
