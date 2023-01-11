from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from app_login.mymngr import MyMgr
from django.utils import timezone  
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    objects = MyMgr()

    student_id = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField(default=timezone.now)  
    is_superuser = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS= ['last_name', 'first_name','address','gender','date_of_birth']

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name



class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dassproj/files/profiles')



    

