from django.urls import path
from . import views

urlpatterns = [
    path("location/", views.addLocation, name="location"),
    path('update/location/<int:pk>/', views.updateLocation, name='updateLocation'), 
    path('delete/location/<int:pk>/', views.deleteLocation, name='deleteLocation'),
    path('install/', views.installation, name='installation'),
    path('update/installation/<int:pk>/', views.updateInstallation, name='updateInstallation'), 
    path('delete/installation/<int:pk>/', views.deleteInstallation, name='deleteInstallation'),
    path("report/", views.report, name="report"),
    path('report/update/<int:pk>/', views.updateReport, name='updateReport'), 
    path('report/delete/<int:pk>/', views.deleteReport, name='deleteReport'),
]
