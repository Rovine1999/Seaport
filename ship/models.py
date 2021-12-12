from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime


class Ship(models.Model):
    name = models.TextField(blank=True, null=True, max_length=200)
    date = models.DateField()
    no_of_containers = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Container(models.Model):
    PRICES = (
        ('112.5', '112.5'),
        ('62', '62')
    )

    SIDES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Free', 'Free')
    )

    SIZES = (
        ('40ft', '40ft'),
        ('20ft', '20ft'),
    )
    
    ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    company_name = models.CharField(max_length=200, blank=True, null=True)
    container_id = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=200, choices=SIZES, default='40ft')
    price = models.CharField(max_length=200, choices=PRICES, default='112.5')
    side = models.CharField(max_length=200, choices=SIDES, default='A')
    status = models.CharField(max_length=200, choices=STATUS, default='Pending')
    comment = models.CharField(max_length=200, default='',)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class Boat(models.Model):
    CHOICES = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid')
    )
    name = models.TextField(blank=True, null=True, max_length=200)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    tone = models.IntegerField(blank=True, null=True)
    date_time= models.DateTimeField()
    status = models.CharField(max_length=10, choices=CHOICES, default='Pending')

    def __str__(self):
        return self.name

