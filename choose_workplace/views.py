from django.shortcuts import render, redirect
from .models import Cabinet, Workplace, BookingDate, BookingWorkplace
from .forms import BookingDateForm, BookingTimeForm, FreeWorkplaceForm
from .functions import find_free_time, analize_time_interval, find_free_workplaces
from django.contrib.auth.models import User

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
            # print(form.data)
            data = {
                'date' : f"{form.data['booking_date_year']}-{form.data['booking_date_month']}-{form.data['booking_date_day']}"
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
    # not_free_workplace_on_this_day = BookingWorkplace.objects.filter(booking_date=date).filter(cabinet=pk).filter(workplace=wkplc).last()
    # if not_free_workplace_on_this_day:
    #     arg = [not_free_workplace_on_this_day.start_time, not_free_workplace_on_this_day.end_time]
    # else: 
    #     arg = None
    # free_time = find_free_time(arg)
    # start_choices = free_time['start']
    # end_choices = free_time['end']
    not_free_workplace_on_this_day = BookingWorkplace.objects.filter(booking_date=date).filter(cabinet=pk).filter(workplace=wkplc)
    default_choices = None
    if not_free_workplace_on_this_day:
        for iter_obj in not_free_workplace_on_this_day:
            arg = [iter_obj.start_time, iter_obj.end_time]
            free_time = find_free_time(arg, default_choices)
            default_choices = free_time['default']
    else: 
        arg = None
        free_time = find_free_time(arg, default_choices)
        default_choices = free_time['default']
    

    start_choices = free_time['start']
    end_choices = free_time['end']
    if len(start_choices) == 0 and len(end_choices) == 0:
        error = 'Данное место в кабинете занято на весь день. Выберете другое место'
    if request.method == 'POST':
        form = BookingTimeForm(request.POST, start_choices=start_choices, end_choices=end_choices, cabinet=pk, workplace=wkplc, booking_date=date, user=request.user)
        if form.is_valid():
            response = form.save(commit=False)
            response.cabinet = pk
            response.workplace = wkplc
            response.booking_date = date
            response.user = request.user.username
            error = analize_time_interval(default_choices, response.start_time, response.end_time)
            if error == '':
                response.save()
                return redirect('successful_booking', pk, wkplc, response.user, date, response.start_time, response.end_time)
        else:
            error = 'Форма была не верной'
        # print('request.user.username', request.user.username)
    form = BookingTimeForm(start_choices=start_choices, end_choices=end_choices, cabinet=pk, workplace=wkplc, booking_date=date, user=request.user) 

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
    # print(request.method)
    if request.method=='POST':
        booking_date = ''
        start_time = ''
        end_time = ''
        form = FreeWorkplaceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('data', data)
            booking_date = data.get('booking_date')
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            return redirect('find_free_workplace', booking_date, start_time, end_time)
    print(booking_date)
    form = FreeWorkplaceForm() 
    # print(args) 
    if all(args):
        table = []
        print('(BookingWorkplace.objects.filter(booking_date=booking_date)', BookingWorkplace.objects.filter(booking_date=booking_date))
        # free_workplaces = find_free_workplaces(BookingWorkplace.objects.filter(booking_date=booking_date), start_time, end_time)
        # print('free_workplaces', free_workplaces)
        # table = Workplace.objects.exclude(cabinet__in=free_workplaces[0], number_wp__in=free_workplaces[1])
        table = find_free_workplaces(Workplace.objects.all(), BookingWorkplace.objects.filter(booking_date=booking_date), start_time, end_time)
#.exclude(number_wp__in=free_workplaces[1])s
        print('table', table)
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



