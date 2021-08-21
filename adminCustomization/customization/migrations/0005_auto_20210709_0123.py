# Generated by Django 3.2.5 on 2021-07-08 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0004_random_font_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='random',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='random',
            name='address',
            field=models.TextField(max_length=400),
        ),
    ]
