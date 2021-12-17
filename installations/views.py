from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages
from .forms import LocationForm, InstallationForm, ReportForm
from .models import Location, Installation, Report

# Create your views here.
@login_required()
def addLocation (request):
    if request.user.is_password_changed: 
        form =  LocationForm()
        paginator = Paginator(Location.objects.all().order_by('-date_added'), 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method == 'POST':
            form = LocationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Added: Location has been added')
                return redirect ('location')
        context = {
            'form': form, 
            'locations': Location.objects.all(),
            'page_obj': page_obj,
        }
        return render (request, 'installations/location.html', context)
    else:
        return redirect('change-password')

@login_required()    
def updateLocation (request, pk):
    if request.user.is_password_changed:
        location = Location.objects.get(id=pk)
        form = LocationForm(instance = location)
        if request.method == 'POST':
            l_form = LocationForm(request.POST, instance = location)
            if l_form.is_valid():
                l_form.save()
                messages.success(request, 'Update: Location has been updated')
                return redirect('location')
        context = {
            'form': form, 
            'installations':Installation.objects.filter(location=location),
            "reports": Report.objects.filter(location=location)
        }
        return render(request, 'installations/location_update.html', context)
    else:
        return redirect('change-password')


@login_required()
def deleteLocation (request, pk):
    if request.user.is_password_changed:
        location = Location.objects.get(pk=pk)
        location.delete()
        messages.success(request, 'Deleted: Location has been deleted')
        return redirect('location')
    else:
        return redirect('change-password')

@login_required()
def installation(request):
    if request.user.is_password_changed:
        form = InstallationForm()
        info = Installation.objects.all()
        paginator = Paginator(Installation.objects.all().order_by('-installation_date'), 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method == 'POST':
            form = InstallationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Added: Installation has been added')
                return redirect('installation')
        context = {
            'form': form, 
            'installations': Installation.objects.all(),
            'page_obj': page_obj,
        }
        return render(request, 'installations/installation.html', context)
    else:
        return redirect('change-password')

@login_required()
def updateInstallation(request, pk):
    if request.user.is_password_changed:
        form = InstallationForm(instance=Installation.objects.get(pk=pk))
        if request.method == 'POST':
            i_form = InstallationForm(request.POST, request.FILES, instance=Installation.objects.get(pk=pk))
            if i_form.is_valid():
                i_form.save()
                messages.success(request, 'Updated: Installation has been updated')
                return redirect('installation')
        context = { 
            'form': form,
            'reports': Report.objects.filter(installation=Installation.objects.get(pk=pk)),
            }
        return render(request, 'installations/installation_update.html', context)
    else:
        return redirect('change-password')

@login_required()
def viewInstallation(request, pk):
    if request.user.is_password_changed:
        installation = Installation.objects.get(pk=pk)
        context = { 
            'installation': installation,
            }
        return render(request, 'installations/installation_view.html', context)
    else:
        return redirect('change-password')

def faultyInstallation(request):
    context = {
        'installations': Installation.objects.filter(equipment_status = 'B')
    }
    return render (request, 'installations/faulty_installation.html', context)

@login_required()
def deleteInstallation (request, pk):
    if request.user.is_password_changed:
        installation = Installation.objects.get(pk=pk)
        installation.delete()
        messages.success(request, 'Deleted: Installation has been deleted')
        return redirect('installation')
    else:
        return redirect('change-password')


@login_required()
def report(request):
    if request.user.is_password_changed:
        form = ReportForm()
        paginator = Paginator(Report.objects.all().order_by('-date'), 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Added: Report has been added')
                return redirect('report')
        context = {
            'form': form, 
            'reports': Report.objects.all(),
            'page_obj': page_obj,
        }
        return render(request, 'installations/report.html', context)
    else:
        return redirect('change-password')

@login_required()
def updateReport(request, pk):
    if request.user.is_password_changed:
        form = ReportForm(instance=Report.objects.get(pk=pk))
        if request.method == 'POST':
            i_form = ReportForm(request.POST, instance=Report.objects.get(pk=pk))
            if i_form.is_valid():
                i_form.save()
                messages.success(request, 'Updated: Report has been updated')
                return redirect('report')
        context = { 'form': form}
        return render(request, 'installations/report_update.html', context)
    else:
        return redirect('change-password')

@login_required()
def deleteReport (request, pk):
    if request.user.is_password_changed:
        report = Report.objects.get(pk=pk)
        report.delete()
        messages.success(request, 'Deleted: Report has been deleted')
        return redirect('report')
    else:
        return redirect('change-password')