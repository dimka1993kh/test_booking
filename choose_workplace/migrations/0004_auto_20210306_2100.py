# Generated by Django 3.1.7 on 2021-03-06 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choose_workplace', '0003_auto_20210305_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdate',
            name='booking_date',
            field=models.DateField(default=datetime.date(2021, 3, 6), verbose_name='Дата бронирования'),
        ),
        migrations.AlterField(
            model_name='bookingworkplace',
            name='booking_date',
            field=models.DateField(default=datetime.date(2021, 3, 6), verbose_name='Дата бронирования'),
        ),
    ]
