from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from rooms.models import Room
from .serializers import RoomSerializer


# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the Room model for using by business.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CustomerRoomViewSet(viewsets.ModelViewSet):
    """
    Viewset for the customer to see available public events and book events
    """
    permission_classes = (AllowAny,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)