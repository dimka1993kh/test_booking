from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cabinet_selection, name='cabinet_selection'),
    path('<int:pk>/', views.choose_workplace, name='choose_workplace'),
    path('<int:pk>/<int:wkplc>/', views.booking_date_workplace, name='booking_date_workplace'),
    path('<int:pk>/<int:wkplc>/booking_<str:date>', views.booking_workplace, name='booking_workplace'),
    path('all_booking/', views.all_booking, name='all_booking'),
    path('all_booking/sort_by_username=<str:username>', views.all_booking, name='all_booking'),
    path('all_booking/sort_by_cabinet=<int:cabinet>', views.all_booking, name='all_booking'),
    path('find_free_workplace', views.find_free_workplace, name='find_free_workplace'),
    path('find_free_workplace?date=<booking_date>_start=<start_time>_end=<end_time>', views.find_free_workplace, name='find_free_workplace')
]