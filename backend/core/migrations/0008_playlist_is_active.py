# Generated by Django 4.2 on 2024-04-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_playlist_schedule_delete_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active'),
        ),
    ]
