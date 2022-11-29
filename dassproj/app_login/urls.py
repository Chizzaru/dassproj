from django.urls import path
from app_trytest import views as formviews

from . import views

urlpatterns = [
    path('',views.login_view,name="login_view"),
    path('login/',views.login_view,name="login_view"),
    path('dashboard/',views.dashboard_view,name="dashboard_view"),
    path('logout/',views.logout_view,name="logout_view"),
    path('dassform/',formviews.get_form,name="get_form"),
    path('submitform/',formviews.submitform,name="submitform"),
    path('registrationform/',views.registration_view,name="registration_view"),

]