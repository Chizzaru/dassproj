from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from app_login.forms import LoginForm, RegistrationForm
from django.contrib.auth import login,logout
from django.urls import reverse

from app_login.models import User
from app_login.mymngr import MyMgr
from app_trytest.models import Result

from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password


from django.contrib import messages

def index_view(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form })

def profiles_view(request):
    current_user = request.user
    userid = current_user.id

    template = loader.get_template('profiles.html')

    HistoryLogs = Result.objects.filter(name_id=userid).order_by('-date')
    context = {}
    if HistoryLogs:
        context = {
            'HistoryLogs'   : HistoryLogs,
            'UserID'        : {
                'id' : current_user.id,
                'student_id' : current_user.student_id,
                'address' : current_user.address,
                'name' : current_user.first_name + ' ' + current_user.middle_name + ' ' + current_user.last_name
            }
        }

    return HttpResponse(template.render(context, request))


def dashboard_view(request):
    current_user = request.user
    userid = current_user.id

    obj= Result.objects.filter(name_id=userid).order_by('-id').first()
    context = {}
    if obj:
        context = {
            'latestresult' : {
                'id' : obj.id,
                'score' : obj.score,
                'depression' : obj.depression,
                'anxiety' : obj.anxiety,
                'stress' : obj.stress,
                'date' : obj.date
            }
    }

    print(context)
    return render(request, "dashboard.html",context)

def form_view(request):
    return render(request, "form.html")

def registration_view(request):
    form = RegistrationForm()
    return render(request, 'registrationform.html', {'form': form })

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect("../dashboard/")# Redirect to a success page.
    else:
        return render(request, 'login.html', {'form': form })
    return render(request, 'login.html', {'form': form })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


#REGISTRATION
def submitregistrationform(request):
    # if this is a POST request we need to process the form data
    form = RegistrationForm(request.POST)
    if(request.POST['password']!=request.POST['repassword']):
        messages.error(request, 'Invalid form submission.')
        messages.error(request, form.errors)

    if form.is_valid():
        obj = User()
        obj.student_id =form.cleaned_data['student_id']
        obj.last_name =form.cleaned_data['last_name']
        obj.first_name =form.cleaned_data['first_name']
        obj.middle_name =form.cleaned_data['middle_name']
        obj.address =form.cleaned_data['address']
        obj.phone_number =form.cleaned_data['phone_number']
        obj.gender =form.cleaned_data['gender']
        obj.date_of_birth =form.cleaned_data['date_of_birth']
        obj.password = make_password(form.cleaned_data['password'])
        obj.is_superuser = False
        obj.is_staff = True
        obj.is_active = False
        obj.save()        
        messages.success(request, 'Registration submitted successfully.')
        return render(request, 'registrationform.html', {'form': RegistrationForm()})
    else:
        form = RegistrationForm()
    return render(request, 'registrationform.html', {'form': form})
    

