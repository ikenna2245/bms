from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.userLogin, name='login'),
    path('clients/', views.clients, name='clients'),
    path('change-password/', views.changePassword, name='change-password'),
    path('user/update/<int:pk>/', views.userUpdate, name='userupdate'), 
    path('user/delete/<int:pk>/', views.deleteUser, name='deleteuser'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='users/home/password_reset.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='users/home/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='users/home/password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/done/", auth_views.PasswordResetCompleteView.as_view(template_name = 'users/home/password_reset_complete.html'), name="password_reset_complete"),
]