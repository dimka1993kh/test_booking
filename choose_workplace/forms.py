from .models import BookingDate, BookingWorkplace
from django.forms import ModelForm, DateInput, Select

class BookingDateForm(ModelForm):
    class Meta:
        model = BookingDate
        fields = ['booking_date']

        widgets = {
                'booking_date' : DateInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Дата бронирования'                    
                }),                                                    
        }

class BookingTimeForm(ModelForm):

    def __init__(self, *args, **kwargs): #, data=None, start_choices=((8,8),), end_choices=((8,8),), cabinet=None, workplace=None, booking_date=None, user=None ,
        print('kwargs', kwargs)
        start_choices = kwargs.pop('start_choices')
        end_choices = kwargs.pop('end_choices')
        super(BookingTimeForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].choices = start_choices
        self.fields['end_time'].choices = end_choices
        
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