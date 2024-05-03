from django.urls import path
from . import views
from .views import view_appointments, give_appointment, doctor_dashboard

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('view-appointments/', view_appointments, name='view_appointments'),
    path('give-appointment/', give_appointment, name='give_appointment'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),

    # Add more URLs as needed
]
