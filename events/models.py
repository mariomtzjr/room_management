from django.db import models

from rest_framework.exceptions import ValidationError

from rooms.models import Room
from customers.models import Customer


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(max_length=255, choices=(("public", "Public"), ("private", "Private")))
    availability = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.customer}: {self.name} on {self.date} in Room {self.room.id}"

    
    def save(self, *args, **kwargs):
        if not self.event_type == 'public':
            raise ValidationError({'event_type': 'This event is private, it cannot be booked.'})

        if not self.room.capacity > 0:
            raise ValidationError({'availability': 'This event is fully booked, no more spaces available.'})
        
        if Event.objects.filter(customer=self.customer.pk).exists():
            events = Event.objects.filter(customer=self.customer.pk)
            for event in events:
                if event.date == self.date:
                    raise ValidationError({'date': 'You already have an event in this day, this event cannot be booked.'})

        self.room.capacity -= 1
        self.availability = self.room.capacity
        self.room.save()
        super().save(*args, **kwargs)
 