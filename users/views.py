from django.shortcuts import render
from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    context = {'segment': 'index'}
    return render(request, 'users/home/index.html', context)

def clients(request):
    form = CustomUserCreationForm()
    context = {
        "form":form, 
        }
    return render(request, 'users/home/page-user.html', context)