from .models import BookingDate, BookingWorkplace
from django.forms import ModelForm, DateInput, Select, DateField, IntegerField, Form, ChoiceField, SelectDateWidget
from .data import default_choices
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput

class BookingDateForm(ModelForm):
    # booking_date = DateField(widget=AdminDateWidget)
    class Meta:
        model = BookingDate
        fields = ['booking_date'] 

        widgets = {
            'booking_date' : SelectDateWidget()
            }  
        # widgets = {
        #     'booking_date' : NumberInput(attrs={'type': 'date'})
        #     }                                                   
        

class BookingTimeForm(ModelForm):

    def __init__(self, *args, **kwargs): 
        # print('kwargs', kwargs)
        start_choices = kwargs.pop('start_choices')
        end_choices = kwargs.pop('end_choices')
        cabinet = kwargs.pop('cabinet')
        workplace = kwargs.pop('workplace')
        booking_date = kwargs.pop('booking_date')
        user = kwargs.pop('user')

        super(BookingTimeForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].choices = start_choices
        self.fields['end_time'].choices = end_choices
        # self.fields['cabinet'].queryset = cabinet
        # self.fields['workplace'].queryset = workplace
        # self.fields['booking_date'].queryset = booking_date
        # self.fields['user'].queryset = user
        
        # if cabinet is not None:
        #     self.fields['cabinet'].initial = cabinet
        # if workplace is not None:
        #     self.fields['workplace'].initial = workplace
        # if booking_date is not None:
        #     self.fields['booking_date'].initial = booking_date
        # if user is not None:
        #     self.fields['user'].initial = user

    class Meta:
        model = BookingWorkplace
        fields = ['start_time', 'end_time'] #, 'cabinet', 'workplace', 'booking_date', 'user'

        widgets = {
                'start_time' : Select(attrs={
                    'class' : 'form-control',               
                }), 
                'end_time' : Select(attrs={
                    'class' : 'form-control',                  
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
            # 'booking_date' : SelectDateWidget()
        }



