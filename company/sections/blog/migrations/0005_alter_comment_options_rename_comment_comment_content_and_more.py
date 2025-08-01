# Generated by Django 5.1.7 on 2025-05-03 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_posted',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment'),
        ),
    ]
