# Generated by Django 4.1.6 on 2023-03-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_hotspots_rfcid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotspots',
            name='gpid',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='hotspots',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotspots',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotspots',
            name='txg',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotspots',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True),
        ),
    ]
