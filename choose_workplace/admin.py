from django.contrib import admin
from .models import Cabinet, Workplace, BookingDate, BookingWorkplace
# Register your models here.
admin.site.register(Cabinet)
admin.site.register(Workplace)
admin.site.register(BookingDate)
admin.site.register(BookingWorkplace)