# Generated by Django 3.2.5 on 2021-07-07 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='random',
            name='font_size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]