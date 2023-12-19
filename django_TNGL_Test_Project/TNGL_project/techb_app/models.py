from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    customer_number = models.CharField(max_length=20, unique=True)
    meter_serial_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

