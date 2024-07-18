from typing import Any
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .managers import FreeTimeSlotsManager


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(help_text="Duration of the service")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="timeslots"
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    free_slots = FreeTimeSlotsManager()  # Custom manager for free time slots
    objects = models.Manager()

    class Meta:
        unique_together = ("service", "date", "start_time", "end_time")

    def clean(self):
        if self.start_time and not self.end_time:
            # ensuring that time slot start and end time match
            # the service duration time and not exceeding it
            if self.service:
                service_duration = self.service.duration
                self.end_time = (
                    datetime.combine(date(1, 1, 1), self.start_time) + service_duration
                ).time()
            else:
                raise ValidationError(
                    "Service must be specified to calculate end_time."
                )

        # Check if both start_time and end_time are set before filtering
        if self.start_time is not None and self.end_time is not None:
            # Checking for overlapping timeslots
            overlapping_time_slots = TimeSlot.objects.filter(
                service=self.service,
                date=self.date,
                start_time__lt=self.end_time,
                end_time__gt=self.start_time,
            ).exclude(id=self.id)

            if overlapping_time_slots.exists():
                raise ValidationError(
                    "This time slot overlaps with another time slot for the same service."
                )

    def __str__(self):
        return f"{self.service.name} on {self.date} from {self.start_time} to {self.end_time}"

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
