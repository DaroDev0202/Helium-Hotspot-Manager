# Generated by Django 4.1.6 on 2023-03-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_hotspots_gpid_alter_hotspots_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotspots',
            name='height',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
    ]
