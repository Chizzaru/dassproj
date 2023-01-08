from django import forms
from django.contrib.auth import authenticate

#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from app_login.models import User, Profile
from app_login.mymngr import MyMgr

class LoginForm(forms.Form):
    student_id = forms.CharField(
        label='Student ID',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'StudentID'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))


    def clean(self):
        student_id = self.cleaned_data.get('student_id')
        password = self.cleaned_data.get('password')
        user = authenticate(student_id=student_id, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        student_id = self.cleaned_data.get('student_id')
        password = self.cleaned_data.get('password')
        user = authenticate(student_id=student_id, password=password)
        return user

    

GENDER = (
    ('Male','Male'),
    ('Female','Female')
)

class UploadImageForm(forms.Form):
    model = Profile
    fields = ('id','image')

class RegistrationForm(forms.Form):
    student_id = forms.CharField(
            max_length=30,
            label="Student ID",
            widget=forms.TextInput(attrs={'name':'studentid','class':'form-control','placeholder':'StudentID','style':'margin-bottom:5px;'})
            )
    last_name = forms.CharField(
            max_length=80,
            label="Lastname",
            widget=forms.TextInput(attrs={'name':'lastname','class':'form-control','placeholder':'Lastname','style':'margin-bottom:5px;'})
            )
    first_name = forms.CharField(
            max_length=80,
            label="Firstname",
            widget=forms.TextInput(attrs={'name':'firstname','class':'form-control','placeholder':'Firstname','style':'margin-bottom:5px;'})
            )
    middle_name = forms.CharField(
            max_length=80,
            label="Middlename",
            widget=forms.TextInput(attrs={'name':'middlename','class':'form-control','placeholder':'Middlename','style':'margin-bottom:5px;'})
            )
    address = forms.CharField(
            max_length=250,
            label="Address",
            widget=forms.TextInput(attrs={'name':'address','class':'form-control','placeholder':'Address','style':'margin-bottom:5px;'})
            )
    phone_number = forms.CharField(
            max_length=20,
            label="Phone Number",
            widget=forms.TextInput(attrs={'name':'phonenumber','class':'form-control','placeholder':'Phone Number','style':'margin-bottom:5px;'})
            )
    gender = forms.ChoiceField(
            choices=GENDER,
            label="Gender",
            widget=forms.Select(attrs={'class':'form-control','style':'margin-bottom:5px;'})
            )
    date_of_birth = forms.CharField(
            label="Date of Birth",
            widget=forms.TextInput(attrs={'name':'dateofbirth','class':'form-control','placeholder':'Date of Birth','type':'date','style':'margin-bottom:5px;'})
            )
    
    password = forms.CharField(
            max_length=100,
            label="Password",
            widget=forms.TextInput(attrs={'name':'password','class':'form-control','placeholder':'Password','style':'margin-bottom:5px;','type':'password'})
            )
    
    repassword = forms.CharField(
            max_length=100,
            label="Confirm Password",
            widget=forms.TextInput(attrs={'name':'repassword','class':'form-control','placeholder':'Confirm Password','style':'margin-bottom:5px;','type':'password'})
            )
    
    '''class Meta:
        model = User
        fields = ('student_id', 'last_name', 'first_name', 'middle_name',
            'address','phone_number','gender','date_of_birth','password',
            'is_superuser','is_staff','is_active')     

    def save(self,commit = True):   
        user = super(MyMgr, self).save(commit = False)
        #user = super(self).save(commit = False)
        user.student_id = self.cleaned_data['student_id']
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.address = self.cleaned_data['address']
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.password = self.cleaned_data['password']
        user.is_superuser = False
        user.is_staff = True
        user.is_active = False

        if commit:
            user.save()

        return user'''
