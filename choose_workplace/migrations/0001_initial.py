# Generated by Django 3.1.7 on 2021-03-03 17:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(default=datetime.date(2021, 3, 3), verbose_name='Дата бронирования')),
            ],
            options={
                'verbose_name': 'Дата бронирования',
                'verbose_name_plural': 'Даты бронирования',
            },
        ),
        migrations.CreateModel(
            name='BookingWorkplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(choices=[], verbose_name='Начало работы')),
                ('end_time', models.IntegerField(choices=[], verbose_name='Окончание работы')),
            ],
            options={
                'verbose_name': 'Время бронирования',
                'verbose_name_plural': 'Время бронирования',
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер кабинета')),
            ],
            options={
                'verbose_name': 'Кабинета',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_wp', models.IntegerField(verbose_name='Номер рабочего места')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='choose_workplace.cabinet', to_field='number')),
            ],
            options={
                'verbose_name': 'Рабочее место',
                'verbose_name_plural': 'Рабочие места',
            },
        ),
    ]
