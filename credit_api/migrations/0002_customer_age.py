# Generated by Django 4.2.16 on 2024-11-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=40),
        ),
    ]
