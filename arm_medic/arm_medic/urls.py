from django.contrib import admin
from django.urls import path
from clinic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('save-appointment/', views.save_appointment_data, name='save_appointment_data'),
    path('select-time/', views.time_selection, name='time_selection'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
]
