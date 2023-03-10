from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Event
from .serializers import EventSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the Event model.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        event.room.capacity += 1
        event.room.save()
        event.delete()
        return Response({})


class CustomerEventViewSet(viewsets.ModelViewSet):
    """
    Viewset for the customer to see available public events and book events
    """
    permission_classes = (AllowAny,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        event.room.capacity += 1
        event.room.save()
        event.delete()
        return Response({})