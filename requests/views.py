from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Request
from .forms import MaintenanceRequestForm
from datetime import *
from django.utils import timezone

def staff(request):
    allRequests = Request.objects.all
    return render(request, 'staff.html', {'all': allRequests})

def tenant(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            newRequest = form.save(commit = False)
            newRequest.dateAndTime = timezone.now()
            newRequest.status = 'Pending'
            newRequest.save()
            form = MaintenanceRequestForm()
    else:
        form = MaintenanceRequestForm()
    return render(request, 'tenant.html', {'form': form})

def update_status(request, request_id):
    maintenance_request = get_object_or_404(Request, pk=request_id)
    if maintenance_request.status == 'Pending':
        maintenance_request.status = 'Completed'
        maintenance_request.save()
    elif maintenance_request.status == 'Completed':
        maintenance_request.status = 'Pending'
        maintenance_request.save()
    allRequests = Request.objects.all
    return render(request, 'staff.html', {'all': allRequests})

def sortNum(request):
    sortedNum= Request.objects.order_by('aptNum')
    return render(request, 'staff.html', {'all': sortedNum})

def sortPending(request):
    pendingRequests = Request.objects.filter(status = 'Pending')
    return render(request, 'staff.html', {'pendingRequests': pendingRequests})

def sortCompleted(request):
    completedRequests = Request.objects.filter(status = 'Completed')
    return render(request, 'staff.html', {'completedRequests': completedRequests})

def filterByArea(request):
    areaFilter = request.POST.get('areaDilter')
    if areaFilter:
        areaRequests = Request.objects.filter(area = areaFilter)
    else:
        areaRequests = Request.objects.filter()
    return render(request, 'staff.html', {'areaRequests': areaRequests})

def filterByDate(request):
    all_requests = Request.objects.order_by('dateAndTime')
    return render(request, 'staff.html', {'all': all_requests})

def addRequest(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.dateAndTime = timezone.now()
            new_request.status = 'Pending'
            new_request.save()
            return render(request, 'tenant.html', {'form': form})

def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Quinn'})
