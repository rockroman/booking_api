from rest_framework import serializers
from .models import Booking
from scheduling.models import TimeSlot,Service
from scheduling.serializers import ServiceSerializer, TimeSlotSerializer 

class BookingCreateSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    time_slot = serializers.PrimaryKeyRelatedField(queryset=TimeSlot.objects.all()) 
    class Meta:
        model = Booking
        fields = [ 'service', 'time_slot',]
        read_only_fields = ['user','status']
        

    def validate(self, attrs):
        # Retrieve the selected service and filter time_slot based on it
        service = attrs.get('service')
        time_slot = attrs.get('time_slot')

        if service and time_slot:
            # Check if the selected time_slot belongs to the selected service
            if time_slot.service != service:
                raise serializers.ValidationError("Selected time slot does not belong to the selected service.")

        return attrs

    def create(self, validated_data):
        # Create and return a new Booking instance
        return Booking.objects.create(**validated_data)
    

class BookingReadSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()   # Serializer for the related Service model
    time_slot = TimeSlotSerializer()   # Serializer for the related TimeSlot model

    class Meta:
        model = Booking
        fields = ['id', 'user', 'service', 'time_slot', 'created_at', 'status']
        read_only_fields = ['id', 'created_at']  # Fields that should not be modified directly

    def validate(self, data):
        # Add any custom validation logic here, if needed
        return data