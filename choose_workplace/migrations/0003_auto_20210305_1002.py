# Generated by Django 3.1.7 on 2021-03-05 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choose_workplace', '0002_auto_20210304_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdate',
            name='booking_date',
            field=models.DateField(default=datetime.date(2021, 3, 5), verbose_name='Дата бронирования'),
        ),
        migrations.AlterField(
            model_name='bookingworkplace',
            name='booking_date',
            field=models.DateField(default=datetime.date(2021, 3, 5), verbose_name='Дата бронирования'),
        ),
    ]
