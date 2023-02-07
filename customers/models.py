from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

