# Generated by Django 2.2.3 on 2020-10-26 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0005_auto_20201025_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='zip',
            field=models.CharField(blank=True, default='93822', max_length=10, null=True),
        ),
    ]
