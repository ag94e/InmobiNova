# Generated by Django 2.2.3 on 2020-10-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0002_auto_20201025_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='name',
            field=models.CharField(blank=True, default='unnamed', max_length=30),
        ),
    ]