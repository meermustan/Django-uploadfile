# Generated by Django 3.0.14 on 2022-03-17 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beasts', '0003_auto_20220317_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='beast',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
