from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ContainerSize(models.Model):
    size = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.size


class ContainerSide(models.Model):
    side = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.side


class ContainerStatus(models.Model):
    COLORS = (
        ('warning', 'warning'),
        ('danger', 'danger'),
        ('success', 'success'),
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('info', 'info')
    )
    status = models.CharField(max_length=10, blank=True, null=True)
    status_color = models.CharField(max_length=10, choices=COLORS, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class Ship(models.Model):
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.TextField(blank=True, null=True, max_length=200)
    date = models.DateField()
    no_of_containers = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Container(models.Model):
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    company_name = models.CharField(max_length=200, blank=True, null=True)
    container_id = models.CharField(max_length=200, blank=True, null=True)
    size = models.ForeignKey(ContainerSize, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.CharField(max_length=200, blank=True, null=True)
    side = models.ForeignKey(ContainerSide, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(ContainerStatus, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

