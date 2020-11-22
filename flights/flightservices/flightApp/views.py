from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authtoken.models import Token
from .models import Baggage, Flight, Passenger, Reservation
from .serializer import (BaggageSerializer, FlightSerializer,
                         PassengerSerializer, UserSerializer,
                         ReservationSerializer)
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView


# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(
        departureCity=request.data['departureCity'],
        arrivalCity=request.data['arrivalCity'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


class BagaggeCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        baggage = Baggage()
        baggage.number = request.data['number']
        if request.user.is_authenticated:
            user = request.user
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        baggage.user = user
        baggage.save()

        baggage_serializer = BaggageSerializer(baggage)
        return Response(baggage_serializer.data,
                        status=status.HTTP_201_CREATED)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class SignUpView(APIView):
    def post(self, request):
        user = User()
        user.password = request.data['password']
        user.username = request.data['username']
        user.save()
        user.set_password(user.password)
        user.save()
        token = Token.objects.get(user_id=user.id)
        user_serializer = UserSerializer(user)
        data = user_serializer.data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated, )


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
