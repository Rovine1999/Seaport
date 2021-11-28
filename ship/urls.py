from django.urls import path
from .views import *
urlpatterns = [
    path('register/new-ship/', registernewship, name='registership'),
    path('register/new-container/<str:ship_id>/<str:ship_name>/', registernewcontainer, name='registercontainer'),
    path('container/edit/<str:container_id>/', editcontainer, name='editcontainer'),
    path('register/new-addons/', registernewaddons, name='addons'),
    path('save/size/', saveSize, name='saveSize'),
    path('save/side/', saveSide, name='saveSide'),
    path('save/status', saveStatus, name='saveStatus'),
    path('shipment/details/<str:ship_id>/<str:ship_name>/', shipdetails, name="shipmentdetails")
]
