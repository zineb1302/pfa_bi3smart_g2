# Generated by Django 5.0.3 on 2024-04-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='champs1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='champs2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='champs3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='champs4',
        ),
        migrations.AddField(
            model_name='profile',
            name='adress',
            field=models.CharField(default='0000-0000-0000', max_length=100),
        ),
    ]