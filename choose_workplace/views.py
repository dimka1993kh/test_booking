from django.shortcuts import render, redirect
from .models import Cabinet, Workplace, BookingDate, BookingWorkplace
from .forms import BookingDateForm, BookingTimeForm
from .functions import find_free_time

# Create your views here.
def choose_workplace(request, pk):
    data = {
        'workplaces' : Workplace.objects.filter(cabinet=pk),
    }
    return render(request, 'choose_workplace/choose_workplace.html', data)

def cabinet_selection(request):
    data = {
        'cabinets' : Cabinet.objects.all()
    }
    return render(request, 'choose_workplace/cabinet_selection.html', data)

def booking_date_workplace(request, pk, wkplc):
    error = ''
    if request.method == 'POST':
        form = BookingDateForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'date' : form.data['booking_date']
            }
            return redirect('booking_workplace', pk, wkplc, data['date'])
        else:
            error = 'Форма была не верной'
    form = BookingDateForm()

    data = {
        'form' : form,
        'cabinet' : pk,
        'workplace' : wkplc
    }
    return render(request, 'choose_workplace/booking_date_workplace.html', data)

def booking_workplace(request, pk, wkplc, date): 
    error = ''
    free_time = find_free_time()
    start_choices = free_time['start']
    end_choices = free_time['end']

    if request.method == 'POST':
        form = BookingTimeForm(request.POST, start_choices=start_choices, end_choices=end_choices)
        print('form_errors', form.errors)
        if form.is_valid():
            response = form.save()
            return redirect('main')
        else:
            error = 'Форма была не верной'
        # print('request.user.username', request.user.username)
    form = BookingTimeForm(start_choices=start_choices, end_choices=end_choices) #, cabinet=pk, workplace=wkplc, booking_date=date, user=request.user.username

    data = {
        'date' : date, 
        'form' : form,
        'cabinet' : pk,
        'workplace' : wkplc,
        'error' : error
        }
    return render(request, 'choose_workplace/booking_workplace.html', data)