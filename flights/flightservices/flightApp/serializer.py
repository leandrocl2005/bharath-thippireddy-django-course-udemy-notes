from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Flight, Passenger, Reservation, Baggage
import re


class BaggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flightNumber(self, value):
        if not re.match("^[a-zA-Z0-9]*$", value):
            raise serializers.ValidationError(
                "Invalid Flight Number, make sure it is a alpha numeric.")
        return value

    def validate(self, data):
        # print(data)
        # print(data['flightNumber'])
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
