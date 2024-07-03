from datetime import datetime, timedelta, time
from .models import Service, TimeSlot

def generate_time_slots(service_id, start_date, end_date):
    service = Service.objects.get(id=service_id)
    duration = service.duration

    # Define working hours (9 AM to 5 PM)
    work_start_time = time(9, 0)
    work_end_time = time(17, 0)

    # Generate time slots for each day in the range
    current_date = start_date
    while current_date <= end_date:
        current_start_time = datetime.combine(current_date, work_start_time)
        current_end_time = datetime.combine(current_date, work_end_time)

        while current_start_time + duration <= current_end_time:
            end_time = (current_start_time + duration).time()
            TimeSlot.objects.create(
                service=service,
                date=current_date,
                start_time=current_start_time.time(),
                end_time=end_time
            )
            current_start_time += duration

        current_date += timedelta(days=1)