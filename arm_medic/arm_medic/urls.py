from django.conf import settings
from django.contrib import admin
from django.templatetags import static
from django.urls import path
from accounts import views as accounts_views
from .views import landing
from staff import views as staff_views
from prescriptions import views as prescriptions_views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    
    path('doctor/', staff_views.doctor_dashboard, name='doctor_dashboard'),
    path('nurse/', staff_views.nurse_dashboard, name='nurse_dashboard'),
    
    path('prescription/create/<int:patient_id>/', 
        prescriptions_views.create_prescription, 
        name='create_prescription'),
    path('prescription/complete/<int:prescription_id>/', 
        prescriptions_views.complete_prescription, 
        name='complete_prescription'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)