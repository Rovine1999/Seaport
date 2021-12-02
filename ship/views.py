from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
# Create your views here.


@login_required(login_url='login')
def shipdetails(request, ship_id, ship_name):
    ship = Ship.objects.get(id=ship_id)
    context = {
        'ship': ship,
        'ships': Ship.objects.all(),
        'containers': Container.objects.filter(ship=ship)
    }
    return render(request, template_name='admin_/shipment/shipdetail.html', context=context)


@login_required(login_url='login')
def registernewship(request):
    shipform = CreateShipForm()

    if request.method == 'POST':
        shipform = CreateShipForm(request.POST)
        if shipform.is_valid():
            shipform.save()
            messages.success(request, 'Ship has been added successfully')
            return redirect('registership')
        else:
            messages.error(request, 'Adding the ship failed')
            return redirect('registership')

    context = {
        'page': 'newship',
        'shipform': shipform
    }
    return render(request, template_name='admin_/shipment/registernewship.html', context=context)

def editship(request, pk):
    ship = get_object_or_404(Ship, id=pk)

    shipform = CreateShipForm(request.POST or None, request.FILES or None, instance=ship)
    
    if request.method == 'POST':
        if shipform.is_valid:
            shipform.save()
            messages.success(request, 'The ship has been updated successfully')
        else:
            messages.error(request, 'Updating the ship failed')
    
    context = {
        'page': 'cont-reg',
        'shipform': shipform
    }
    return render(request, template_name='admin_/shipment/editship.html', context=context)

def deleteship(request, pk):
    ship = Ship.objects.get(id=pk)
    ship.delete()
    return redirect ('home')

@login_required(login_url='login')
def registernewcontainer(request, ship_id, ship_name):
    ship = Ship.objects.get(id=ship_id)
    containerform = CreateContainerForm()

    if request.method == 'POST':
        containerform = CreateContainerForm(request.POST)
        if containerform.is_valid():
            instance = containerform.save(commit=False)
            instance.ship = ship
            instance.save()
            messages.success(request, 'The Container has been added successfully')
            return redirect('shipmentdetails', ship_id=ship_id, ship_name=ship_name)
        else:
            messages.error(request, 'Adding the container failed')
            return redirect('shipmentdetails', ship_id=ship_id, ship_name=ship_name)

    context = {
        'page': 'cont-reg',
        'containerform': containerform
    }
    return render(request, template_name='admin_/shipment/registernewcontainer.html', context=context)

@login_required(login_url='login')
def editcontainer(request, container_id):

    container = get_object_or_404(Container, id=container_id)

    containerform = CreateContainerForm(request.POST or None, request.FILES or None, instance=container)
    
    if request.method == 'POST':
        if containerform.is_valid:
            containerform.instance.ship = container.ship
            containerform.save()
            messages.success(request, 'The Container has been updated successfully')
            
        else:
            messages.error(request, 'Updating the container failed')

    context = {
        'page': 'cont-reg',
        'containerform': containerform,
       
    }
    return render(request, template_name='admin_/shipment/editcontainer.html', context=context)

def containerdelete(request, pk):
    container = container.objects.get(id=pk)
    container.delete()
    return redirect ('home')


@login_required(login_url='login')
def registernewaddons(request):
    sizeform = CreateSizeForm()
    sideform = CreateSideForm()
    statusform = CreateStatusForm()
    boatform = CreateBoatForm()
    context = {
        'page': 'addons-reg',
        'sizeform': sizeform,
        'sideform': sideform,
        'statusform': statusform,
        'boatform' : boatform
    }
    return render(request, template_name='admin_/shipment/registeraddons.html', context=context)


@login_required(login_url='login')
def saveSize(request):
    if request.method == 'POST':
        sizeform = CreateSizeForm(request.POST)
        if sizeform.is_valid():
            sizeform.save()
            messages.success(request, 'Size has been added successfully')
            return redirect('addons')
        else:
            messages.error(request, 'Adding the size failed')
            return redirect('addons')

    else:
        messages.error(request, 'Unverified request method')
        return redirect('addons')


@login_required(login_url='login')
def saveSide(request):
    if request.method == 'POST':
        sideform = CreateSideForm(request.POST)
        if sideform.is_valid():
            sideform.save()
            messages.success(request, 'Side has been added successfully')
            return redirect('addons')
        else:
            messages.error(request, 'Adding the side failed')
            return redirect('addons')

    else:
        messages.error(request, 'Unverified request method')
        return redirect('addons')


@login_required(login_url='login')
def saveStatus(request):
    if request.method == 'POST':
        statusform = CreateStatusForm(request.POST)
        if statusform.is_valid():
            statusform.save()
            messages.success(request, 'Status has been added successfully')
            return redirect('addons')
        else:
            messages.error(request, 'Adding the status failed')
            return redirect('addons')

    else:
        messages.error(request, 'Unverified request method')
        return redirect('addons')

@login_required(login_url='login')
def saveboat(request):
    if request.method == 'POST':
        boatform = CreateBoatForm(request.POST)
        if boatform.is_valid():
            boatform.save()
            messages.success(request, 'Boat has been added successfully')
            return redirect('addons')
        else:
            messages.error(request, 'Adding the boat failed')
            return redirect('addons')

    else:
        messages.error(request, 'Unverified request method')
        return redirect('addons')