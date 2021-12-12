from django.urls import path
from .views import *
urlpatterns = [
    path('register/new-ship/', registernewship, name='registership'),
    path('register/new-container/<str:ship_id>/<str:ship_name>/', registernewcontainer, name='registercontainer'),
    path('container/edit/<str:container_id>/', editcontainer, name='editcontainer'),
    path('register/new-boat/', registernewboat, name='registerboat'),
    path('shipment/details/<str:ship_id>/<str:ship_name>/', shipdetails, name="shipmentdetails"),
    path('container/delete/<str:pk>/', containerdelete, name="containerdelete"),
    path('ship/delete/<str:pk>/', deleteship, name="deleteship"),
    path('ship/edit/<str:pk>/', editship, name='editship'),
    path('boat/edit/<str:pk>/', editboat, name='editboat'),
    path('boat/delete/<str:pk>/', deleteboat, name="deleteboat"),
]
