from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from ship.models import Ship, Boat


@login_required(login_url='login')
def home(request):

    context = {
        'page': 'dashboard',
        'ships': Ship.objects.all(),
        'boats': Boat.objects.filter()
    }
    return render(request, template_name='admin_/index.html', context=context)
