from django.shortcuts import render

from rest_framework import viewsets

from rooms.models import Room
from .serializers import RoomSerializer


# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the Room model.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer