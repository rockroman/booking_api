from .models import Service,TimeSlot
from rest_framework import serializers
from datetime import timedelta



class ServiceSerializer(serializers.ModelSerializer):
    duration_minutes = serializers.IntegerField(write_only=True, help_text="Duration of the service in minutes")

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'duration_minutes', 'price']
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['duration_minutes'] = int(instance.duration.total_seconds() // 60)
        return representation

    def validate(self, data):
        duration_minutes = data.pop('duration_minutes', None)  # Remove 'duration_minutes' from data
        if duration_minutes is None:
            raise serializers.ValidationError("Duration in minutes is required.")
        if duration_minutes <= 0:
            raise serializers.ValidationError("Duration in minutes is needs to be greater than 0.")
            
        data['duration'] = timedelta(minutes=duration_minutes)
        return data

    def create(self, validated_data):
        duration = validated_data.pop('duration', None)  # Remove 'duration' from validated_data
        return Service.objects.create(**validated_data, duration=duration)

    def update(self, instance, validated_data):
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
    
    
class TimeSlotSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = TimeSlot
        fields = '__all__'