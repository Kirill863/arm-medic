from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from staff import views as staff_views
from prescriptions import views as prescriptions_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.user_login, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.user_login, name='login'),
    
    path('doctor/', staff_views.doctor_dashboard, name='doctor_dashboard'),
    path('nurse/', staff_views.nurse_dashboard, name='nurse_dashboard'),
    
    path('prescription/create/<int:patient_id>/', 
        prescriptions_views.create_prescription, 
        name='create_prescription'),
    path('prescription/complete/<int:prescription_id>/', 
        prescriptions_views.complete_prescription, 
        name='complete_prescription'),
]