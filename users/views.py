from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib import messages


# Create your views here.

def index(request):
    context = {'segment': 'index'}
    return render(request, 'users/home/index.html', context)

def clients(request):
    form = CustomUserCreationForm()
    users = CustomUser.objects.all()
    paginator = Paginator(CustomUser.objects.all(), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            print("usersaved")
            messages.success(request, "New profile has been added")
            return redirect('clients')
    context = {
        'form':form, 
        'users':users,
        'page_obj': page_obj,
        }
    return render(request, 'users/home/page-user.html', context)

def locations(request):
    context = {'segment': 'index'}
    return render(request, 'users/home/')