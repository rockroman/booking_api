from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Booking
from .serializers import BookingReadSerializer, BookingCreateSerializer

class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':  #  creating a new booking
            return BookingCreateSerializer
        return BookingReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
