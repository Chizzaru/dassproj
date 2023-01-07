from django.urls import path
from . import views

urlpatterns = [
    path('dassform/',views.get_form, name="dassform"),
    path('submitform/',views.submitform,name="submitform"),
    path('deletelogs/',views.deletelogs, name="deletelogs"),
    path('clearAllLogs/<action>',views.clearAllLogs, name="clearAllLogs")
]