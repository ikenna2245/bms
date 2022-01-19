from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from installations.models import Location, Installation, Report
from .tasks import send_registration_email_task
from django.db.models.functions import TruncMonth
from django.db.models import Count

# Create your views here.
@login_required()
def index(request):
    if request.user.is_password_changed:
        info = Installation.objects.annotate(month=TruncMonth('installation_date')).values('month').annotate(c=Count('id')).order_by('month')
        context = {
            'clients': CustomUser.objects.filter(user_status='C').count(),
            'locations': Location.objects.all().count(),
            'report': Report.objects.all().count(),
            'faulty_installations': Installation.objects.filter(equipment_status = 'B').count(),
            'staffs': CustomUser.objects.filter(user_status='S').count(),
            'installations': Installation.objects.all().order_by('-installation_date')[:5],
            'locations_all': Location.objects.all().order_by('-date_added')[:5],
            'UPS' : Installation.objects.filter(equipment_type = 'UPS').count(),  
            'UPS_Battery': Installation.objects.filter(equipment_type = 'UB').count(),  
            'Power_Inverter': Installation.objects.filter(equipment_type = 'PI').count(),  
            'Power_Inverter_Battery': Installation.objects.filter(equipment_type = 'IB').count(), 
            'Surge_Protector': Installation.objects.filter(equipment_type = 'SP').count(),  
            'Power_Generator': Installation.objects.filter(equipment_type = 'PG').count(), 
            'Voltage_Regulator ': Installation.objects.filter(equipment_type = 'VR').count(), 
            'Bypass_Switch': Installation.objects.filter(equipment_type = 'BS').count(),  
            'Solar_Panel ': Installation.objects.filter(equipment_type = 'SOP').count(),  
            'Others': Installation.objects.filter(equipment_type = 'OT').count(), 
            'info':info,
        }
        return render(request, 'users/home/index.html', context)
    else:
        return redirect('change-password')

@login_required()
def clients(request):
    if request.user.is_password_changed:
        form = CustomUserCreationForm()
        users = CustomUser.objects.all()
        paginator = Paginator(CustomUser.objects.all().order_by('-date_joined'), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "New user has been created")
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                first_name = form.cleaned_data.get('first_name')
                send_registration_email_task.delay(email, password, first_name)
                return redirect('clients')
        context = {
            'form':form, 
            'users':users,
            'page_obj': page_obj,
            }
        return render(request, 'users/home/page-user.html', context)
    else:
        return redirect('change-password')

@login_required()
def userUpdate(request, pk):
    form = CustomUserChangeForm(instance = CustomUser.objects.get(pk=pk))
    if request.method == 'POST':
        p_form =  CustomUserChangeForm(request.POST, instance = CustomUser.objects.get(pk=pk))
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'User update was successful')
            return redirect('clients')
    context = {
        'form': form, 
        'locations': Location.objects.filter(clients=CustomUser.objects.get(pk=pk))
    }
    return render(request, 'users/home/user-update.html', context)

@login_required()    
def deleteUser(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    messages.success(request, 'User was deleted successfully')
    return redirect('clients')


def userLogin (request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_password_changed:
                    return redirect('index')
                else:
                    return redirect('change-password')
            else:
                messages.error(request, "invalid User detail")
                return render(request, 'users/home/login.html')
    return render(request, 'users/home/login.html')


@login_required()
def changePassword (request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed Successfullly')
            user = CustomUser.objects.get(pk=request.user.id)
            user.is_password_changed = True
            user.save()
            return redirect ('index')
        messages.info(request, "Invalid password")
        return redirect ('change-password')
    else:
        context = {
            "form": PasswordChangeForm(user=request.user)
        }
        return render(request, 'users/home/change-password.html', context) 

def userLogout(request):
    logout(request)
    return redirect('login')

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request, exception=None):
    return render(request, '500.html')

def error_403(request, exception=None):
    return render(request, '403.html')