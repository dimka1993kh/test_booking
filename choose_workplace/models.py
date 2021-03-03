from django.db import models
import datetime
from .data import default_choices

# Create your models here.
class Cabinet(models.Model):
    number = models.IntegerField('Номер кабинета', unique=True)
    def __str__(self):
        return f'Кабинет номер {self.number}'

    class Meta:
            verbose_name = 'Кабинета'
            verbose_name_plural = 'Кабинеты'
    

class Workplace(models.Model):
    number_wp = models.IntegerField('Номер рабочего места')
    cabinet = models.ForeignKey(Cabinet, on_delete=models.PROTECT, to_field='number')

    def __str__(self):
        return f'Кабинет {self.cabinet}, рабочее место номер {self.number_wp}'

    class Meta:
            verbose_name = 'Рабочее место'
            verbose_name_plural = 'Рабочие места'

class BookingDate(models.Model):
    booking_date = models.DateField('Дата бронирования', default=datetime.date.today())
    
    def __str__(self):
        return f'Дата бронирования {self.booking_date}'

    class Meta:
            verbose_name = 'Дата бронирования'
            verbose_name_plural = 'Даты бронирования'

class BookingWorkplace(models.Model):

    # user = models.CharField('Пользователь', max_length=250, default='')


    # cabinet = models.OneToOneField(Cabinet, on_delete=models.PROTECT, to_field='number')
    # workplace = models.OneToOneField(Workplace, on_delete=models.PROTECT, to_field='number_wp')
    # booking_date = models.OneToOneField(BookingDate, on_delete=models.PROTECT, to_field='booking_date')
    
    
    # cabinet = models.IntegerField('Номер кабинета', default=0)
    # workplace = models.IntegerField('Номер рабочего места', default=0)
    # booking_date = models.DateField('Дата бронирования', default=datetime.date.today())

    start_time = models.IntegerField('Начало работы', choices=default_choices)
    end_time = models.IntegerField('Окончание работы', choices=default_choices)

    def __str__(self):
        return f'Начало работы {self.start_time}, окончание работы {self.end_time}'

    class Meta:
            verbose_name = 'Время бронирования'
            verbose_name_plural = 'Время бронирования'
    

