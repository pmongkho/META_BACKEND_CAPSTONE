from django.utils import timezone
from django.db import models
from datetime import date, datetime

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    table_no = models.IntegerField(default=0)
    no_of_guests = models.IntegerField()
    booking_datetime = models.DateTimeField()

    class Meta:
        unique_together = ('booking_datetime', 'table_no',)
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

        
    
    