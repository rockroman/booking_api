from django.contrib import admin
from .models import Service,TimeSlot
# from .forms import TimeSlotForm

class TimeSlotAdmin(admin.ModelAdmin):
    readonly_fields = ['end_time']  # Make end_time read-only
# class TimeSlotAdmin(admin.ModelAdmin):
#     form = TimeSlotForm
#     list_display = ['service', 'date', 'start_time', 'end_time']
#     list_filter = ['service', 'date']
#     search_fields = ['service__name']

admin.site.register(Service)
admin.site.register(TimeSlot,TimeSlotAdmin)
