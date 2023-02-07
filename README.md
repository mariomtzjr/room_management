# Room Management API

A Django REST framework based API for managing a business focused on renting different rooms for events.

## Requirements
- There are N rooms with M capacity.
- There are two types of events: public and private.
- If the event is public, any customer can book a space.
- If the event is private, no one else can book a space in the room.
- A customer can book a space for an event, if the event is public and there is still space available.
- A customer can cancel its booking and their space should be available again.
- A customer cannot book a space twice for the same event.

## Features
- The business can create a room with M capacity.
- The business can create events for every room.
- The business can delete a room if said room does not have any events.
- A customer can book a place for an event.
- A customer can cancel its booking for an event.
- A customer can see all the available public events.

## Considerations
- For now, there is only one event per day.
- Each room has a different capacity.

## Endpoints
The following endpoints are available in the API:

- /rooms/: To create, retrieve, update and delete rooms.
- /events/: To create, retrieve, update and delete events.
- /customers/: To create, retrieve, update and delete customers.

## Installation
1. Clone the repository: git clone git@github.com:mariomtzjr/room_management.git
2. Install the required packages: pip install -r requirements.txt
3. Run migrations: python manage.py migrate
4. Run the development server: python3 manage.py runserver