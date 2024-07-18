from django.db import models
from django.conf import settings
from scheduling.models import Service, TimeSlot


class Booking(models.Model):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (CANCELLED, "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="bookings"
    )
    time_slot = models.ForeignKey(
        TimeSlot, on_delete=models.CASCADE, related_name="bookings"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    # make sure that each user can book a service in a specific time slot only once
    class Meta:
        unique_together = ("user", "service", "time_slot")

    def __str__(self):
        return f"Booking by {self.user.username} for {self.service.name} on {self.time_slot.date} from {self.time_slot.start_time} to {self.time_slot.end_time}"
