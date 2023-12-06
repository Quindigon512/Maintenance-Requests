from django.db import models
from django.utils import timezone
from PIL import Image

class Request(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    aptNum = models.IntegerField()
    area = models.CharField(max_length = 50)
    descr = models.CharField(max_length = 2000)
    dateAndTime = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to = "images/")
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.area
    
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    phoneNum = models.CharField(max_length=20)
    email = models.EmailField()
    checkIn = models.DateField()
    checkOut = models.DateField(null=True, blank=True)
    aptNum = models.CharField(max_length=10)

    def __str__(self):
        return self.name
