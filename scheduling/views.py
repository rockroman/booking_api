from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service,TimeSlot
from .serializers import ServiceSerializer,TimeSlotSerializer
from rest_framework import status, permissions, generics

# Create your views here.


class ServiceList(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Service.objects.all()
    
    

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Service.objects.all()
    
