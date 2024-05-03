# Generated by Django 5.0.4 on 2024-05-01 10:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.CharField(max_length=50),
        ),
    ]
