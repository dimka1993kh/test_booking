from .models import BookingDate, BookingWorkplace
from django.forms import ModelForm, DateInput, Select, DateField, IntegerField, Form, ChoiceField, SelectDateWidget
from .data import default_choices
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput
from bootstrap_datepicker_plus import DatePickerInput

class BookingDateForm(ModelForm):
    class Meta:
        model = BookingDate
        fields = ['booking_date'] 

        widgets = {
            'booking_date' : SelectDateWidget()
            }                                                   



class BookingTimeForm(ModelForm):
    def __init__(self, *args, **kwargs): 
        start_choices = kwargs.pop('start_choices')
        end_choices = kwargs.pop('end_choices')
        cabinet = kwargs.pop('cabinet')
        workplace = kwargs.pop('workplace')
        booking_date = kwargs.pop('booking_date')
        user = kwargs.pop('user')

        super(BookingTimeForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].choices = start_choices
        self.fields['end_time'].choices = end_choices

    class Meta:
        model = BookingWorkplace
        fields = ['start_time', 'end_time']
        widgets = {
                'start_time' : Select(attrs={
                    'class' : 'form-select',
                    'aria-label' : "Default select example",             
                }), 
                'end_time' : Select(attrs={
                    'class' : 'form-select',
                    'aria-label' : "Default select example",                   
                }),                                                    
        }

class FreeWorkplaceForm(Form):
    booking_date = DateField(label='Дата', widget=SelectDateWidget())
    start_time = ChoiceField(label='Начало работы', choices=default_choices)
    end_time = ChoiceField(label='Конец работы', choices=default_choices)
    class Meta:
        fields = ['booking_date', 'start_time', 'end_time']
        widgets = {
            'start_time' : Select(attrs={
            'class' : 'form-control', 
            'verbose_name' : 'Начало'              
            }), 
            'end_time' : Select(attrs={
            'class' : 'form-control',                  
            }),  
        }



