# Generated by Django 5.1.7 on 2025-05-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_alter_notification_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('alert', 'Alert'), ('invite', 'Invite'), ('request', 'Request'), ('reminder', 'Reminder'), ('update', 'Update'), ('warning', 'Warning'), ('info', 'Info'), ('error', 'Error'), ('success', 'Success'), ('message', 'Message'), ('like', 'Like'), ('comment', 'Comment')], default='alert', max_length=20),
        ),
    ]
