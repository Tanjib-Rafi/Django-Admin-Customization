# Generated by Django 3.2.5 on 2021-07-08 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0005_auto_20210709_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='random',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
