# Generated by Django 2.2.1 on 2020-01-23 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0007_auto_20200115_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='numbers',
            field=models.PositiveIntegerField(default=0),
        ),
    ]