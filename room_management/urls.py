"""room_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from rooms.views import RoomViewSet, CustomerRoomViewSet
from events.views import EventViewSet, CustomerEventViewSet
from customers.views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'business/rooms', RoomViewSet)
router.register(r'customer/rooms', CustomerRoomViewSet)

router.register(r'business/events', EventViewSet)
router.register(r'customer/events', CustomerEventViewSet)
router.register(r'customers', CustomerEventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = router.urls



