# Generated by Django 5.0.2 on 2024-02-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_localisation',
            name='nom_departement',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]