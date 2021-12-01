from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from installations.models import Location
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
@login_required()
def index(request):
    if request.user.is_password_changed:
        return render(request, 'users/home/index.html')
    else:
        return redirect('change-password')

@login_required()
def clients(request):
    if request.user.is_password_changed:
        form = CustomUserCreationForm()
        users = CustomUser.objects.all()
        paginator = Paginator(CustomUser.objects.all(), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "New profile has been added")
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
                messages.success(request, "invalid User detail")
                print('failed authentication')
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
            "form": PasswordChangeForm(user=request.user).as_p
        }
        return render(request, 'users/home/change-password.html', context) 

def userLogout(request):
    logout(request)
    return redirect('login')
