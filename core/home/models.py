from email.mime import image
from django.db import models

# Signals (if needed in future)
from django.db.models.signals import post_save
# Receiver decorator for signals
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self)->str:
        return self.car_name

# Signal receiver for Car model post_save
@receiver(post_save, sender=Car)
def car_call_api(sender, instance, **kwargs):
    print("CAR OBJECT CREATED/SAVED:")
    print(sender, instance, kwargs)