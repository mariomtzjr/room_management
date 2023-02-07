from rest_framework import viewsets

from customers.models import Customer
from .serializers import CustomerSerializer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the Customer model.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer