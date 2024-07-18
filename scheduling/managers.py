from django.db import models


class FreeTimeSlotsManager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        from booking.models import Booking

        return (
            super()
            .get_queryset()
            .exclude(id__in=Booking.objects.values("time_slot_id"))
        )
