# Generated by Django 5.0.2 on 2024-02-09 08:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
