# Generated by Django 4.1.3 on 2022-12-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='location',
        ),
    ]
