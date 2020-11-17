# Generated by Django 2.2.3 on 2020-10-28 21:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0010_auto_20201027_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='houses',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='image',
            field=models.CharField(blank=True, default='https://imgurl.me/images/2020/10/28/NOIMAGEabcdc93a3d26c769.png', max_length=600),
        ),
    ]