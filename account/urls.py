from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
]
