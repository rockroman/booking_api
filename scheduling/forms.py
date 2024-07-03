
# from django import forms
# from .models import TimeSlot
# from datetime import datetime, timedelta

# class TimeSlotForm(forms.ModelForm):
#     class Meta:
#         model = TimeSlot
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         instance = kwargs.get('instance')
#         if instance and instance.service:
#             service_duration = instance.service.duration
#             if instance.start_time:
#                 start_time = datetime.combine(datetime.today(), instance.start_time)
#                 self.fields['end_time'].initial = (start_time + service_duration).time()

#         # Add help text to end_time field
#         self.fields['end_time'].help_text = "Automatically calculated based on start time and service duration."

#     def clean(self):
#         cleaned_data = super().clean()
#         start_time = cleaned_data.get('start_time')
#         service = cleaned_data.get('service')

#         if start_time and service:
#             service_duration = service.duration
#             cleaned_data['end_time'] = (datetime.combine(datetime.today(), start_time) + service_duration).time()

#         return cleaned_data