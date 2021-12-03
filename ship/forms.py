from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class CreateShipForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'placeholder': 'Ship Name'}),
        label='Ship Name')

    date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'date'}),
        label='Date')

    no_of_containers = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'placeholder': 'No of Containers'}),
        label='Number of Containers')

    class Meta:
        model = Ship
        fields = ['name', 'date', 'no_of_containers']

        # widgets = {
        #     'name': forms.CharField(attrs={'class': ''})
        # }

class CreateBoatForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Boat Name'}),
        label='Boat Name')

    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Company Name'}),
        label='Company Name')

    tone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Tones'}),
        label='Tones')

    date_time = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'datetime-local', 'placeholder': 'Date of Arrival'}),
        label='Date of Arrival')

    status = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text'}),
        label='Status')

    class Meta:
        model = Boat
        fields = ['name', 'company_name', 'tone', 'date_time', 'status']


class CreateContainerForm(forms.ModelForm):
    date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'date'}),
        label='Date')

    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Company Name'}),
        label='Company Name')

    # price = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Ksh 120000'}),
    #     label='Price')

    container_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Container ID'}),
        label='Container ID')

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control shadow-none', 'type': 'text', 'placeholder': 'Comment about container', 'rows': '5'}),
        label='Comment About Container')

    class Meta:
        model = Container
        fields = ['date', 'company_name', 'container_id', 'size', 'price', 'side', 'status', 'comment']

        widgets = {
            'size': forms.Select(attrs={'class': 'form-select shadow-none'}),
            'side': forms.Select(attrs={'class': 'form-select shadow-none'}),
            'status': forms.Select(attrs={'class': 'form-select shadow-none'}),

        }

        price = {
            'size': forms.Select(attrs={'class': 'form-select shadow-none'}),
            'side': forms.Select(attrs={'class': 'form-select shadow-none'}),
            'status': forms.Select(attrs={'class': 'form-select shadow-none'}),

        }


class CreateSizeForm(forms.ModelForm):
    size = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text'}),
        label='Size')

    class Meta:
        model = ContainerSize
        fields = ['size']


class CreateSideForm(forms.ModelForm):
    side = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text'}),
        label='Side')

    class Meta:
        model = ContainerSide
        fields = ['side']


class CreateStatusForm(forms.ModelForm):
    status = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control shadow-none', 'type': 'text'}),
        label='Status')

    class Meta:
        model = ContainerStatus
        fields = ['status', 'status_color']

        widgets = {
            'status_color': forms.Select(attrs={'class': 'form-select shadow-none'}),
        }
