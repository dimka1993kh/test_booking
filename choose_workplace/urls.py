from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cabinet_selection, name='cabinet_selection'),
    path('<int:pk>/', views.choose_workplace, name='choose_workplace'),
    path('<int:pk>/<int:wkplc>/', views.booking_date_workplace, name='booking_date_workplace'),
    path('<int:pk>/<int:wkplc>/booking_<str:date>', views.booking_workplace, name='booking_workplace'),
    path('all_booking', views.all_booking, name='all_booking')
]