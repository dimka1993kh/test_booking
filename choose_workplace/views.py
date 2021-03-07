from django.shortcuts import render, redirect
from .models import Cabinet, Workplace, BookingWorkplace
from .forms import BookingDateForm, BookingTimeForm, FreeWorkplaceForm
from .functions import find_free_time, analize_time_interval, find_free_workplaces
from django.contrib.auth.models import User
from .data import default_choices

# Create your views here.
def choose_workplace(request, pk):
    data = {
        'workplaces' : Workplace.objects.filter(cabinet=pk),
        'cabinet' : pk
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
            date = f"{form.data['booking_date_year']}-{form.data['booking_date_month']}-{form.data['booking_date_day']}"
            return redirect('booking_workplace', pk, wkplc, date)
        else:
            error = 'Форма была не верной'
    form = BookingDateForm()
    data = {
        'form' : form,
        'cabinet' : pk,
        'workplace' : wkplc
    }
    return render(request, 'choose_workplace/booking_date_workplace.html', data)

def booking_workplace(request, pk, wkplc, date, start_time=None, end_time=None): 
    error = ''
    not_free_workplace_on_this_day = BookingWorkplace.objects.filter(booking_date=date).filter(cabinet=pk).filter(workplace=wkplc)
    now_choices = None
    if not_free_workplace_on_this_day:
        for workplace in not_free_workplace_on_this_day:
            arg = [workplace.start_time, workplace.end_time]
            free_time = find_free_time(arg, now_choices)
            now_choices = free_time['default']
    else: 
        arg = None
        free_time = find_free_time(arg, now_choices)
        now_choices = free_time['default']

    start_choices = free_time['start']
    end_choices = free_time['end']
    if now_choices == []:
        error = 'Данное место в кабинете занято на весь день. Выберете другое место'
        data = {
            'date' : date, 
            'cabinet' : pk,
            'workplace' : wkplc,
            'user': request.user,
            'error' : error,
            }
    else:
        if request.method == 'POST':
            form = BookingTimeForm(request.POST, start_choices=start_choices, end_choices=end_choices, cabinet=pk, workplace=wkplc, booking_date=date, user=request.user)
            if form.is_valid():
                response = form.save(commit=False)
                response.cabinet = pk
                response.workplace = wkplc
                response.booking_date = date
                response.user = request.user.username
                error = analize_time_interval(default_choices, now_choices, response.start_time, response.end_time, BookingWorkplace.objects.filter(booking_date=date).filter(cabinet=pk))
                if error == '':
                    response.save()
                    return redirect('successful_booking', pk, wkplc, response.user, date, response.start_time, response.end_time)
            else:
                error = 'Форма была не верной'
        form = BookingTimeForm(request.POST, start_choices=start_choices, end_choices=end_choices, cabinet=pk, workplace=wkplc, booking_date=date, user=request.user) 
        data = {
            'date' : date, 
            'form' : form,
            'cabinet' : pk,
            'workplace' : wkplc,
            'user': request.user,
            'error' : error,
            }
    return render(request, 'choose_workplace/booking_workplace.html', data)

def all_booking(request, username=None, cabinet=None):
    if username:
        table = BookingWorkplace.objects.filter(user=username)
    elif cabinet:
        table = BookingWorkplace.objects.filter(cabinet=cabinet)
    else:
        table = BookingWorkplace.objects.all()
    data = {
        'table' : table,
        'cabinets': Cabinet.objects.all(),
        'users' : User.objects.all()
    }
    return render(request, 'choose_workplace/all_booking.html', data)

def find_free_workplace(request, booking_date=None, start_time=None, end_time=None):
    args = [booking_date != None, start_time != None, end_time != None]
    if request.method=='POST':
        booking_date = ''
        start_time = ''
        end_time = ''
        form = FreeWorkplaceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            booking_date = data.get('booking_date')
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            return redirect('find_free_workplace', booking_date, start_time, end_time)
    form = FreeWorkplaceForm() 
    if all(args):
        # error = analize_time_interval(default_choices, now_choices, response.start_time, response.end_time, BookingWorkplace.objects.filter(booking_date=date))
        table = find_free_workplaces(Workplace.objects.all(), BookingWorkplace.objects.filter(booking_date=booking_date), start_time, end_time)
    else:
        table = Workplace.objects.all()
    data = {
        'form' : form,
        'booking_date' : booking_date, 
        'start_time' : start_time, 
        'end_time' : end_time,
        'table' : table
    }
    return render(request, 'choose_workplace/find_free_workplace.html', data)

def successful_booking(request, pk, wkplc, username, start_time, end_time, date):
    data = {
        'cabinet' : pk,
        'workplace' : wkplc,
        'username' : username,
        'start_time' : start_time,
        'end_time' : end_time, 
        'date' : date
    }
    return render(request, 'choose_workplace/successful_booking.html', data)



