# Generated by Django 4.1.3 on 2022-12-02 16:06

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326),
        ),
    ]