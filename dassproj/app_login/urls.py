from django.urls import path
from app_trytest import views as formviews

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.login_view,name="login_view"),
    path('login/',views.login_view,name="login_view"),
    path('dashboard/',views.dashboard_view,name="dashboard_view"),
    path('profiles/',views.profiles_view,name="profiles_view"),
    path('results/',views.resultpage_view,name="resultpage_view"),
    path('logout/',views.logout_view,name="logout_view"),
    path('uploadimage/',views.upload_image,name="upload_image"),
    path('dassform/',formviews.get_form,name="get_form"),
    path('dassform/submitform/',formviews.submitform,name="submitform"),
    path('deletelogs/',formviews.deletelogs,name="deletelogs"),
    path('deletelog/<str:result_id>',formviews.deletelog,name="deletelog"),
    path('clearAllLogs/<action>',formviews.clearAllLogs,name="clearAllLogs"),
    path('registrationform/',views.registration_view,name="registration_view"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)