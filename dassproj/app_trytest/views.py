from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question, Choice, Answer, Result
from django.urls import reverse
from .operations import getResultAnxiety, getResultDepression, getResultStress, DASS21_compute
import datetime


from .randomforest import randomForestAnxiety, randomForestDepression, randomForestStress

from django.contrib.messages import constants as messages



def get_form(request):
    current_user = request.user

    myQuestions = Question.objects.all().values()
    myChoices = Choice.objects.all().values()
    template = loader.get_template('form.html')
    context = {
        'myQuestions'   : myQuestions,
        'myChoices'     : myChoices,
        'UserID'        : {
            'id' : current_user.id,
            'student_id' : current_user.student_id,
            'name' : current_user.first_name + ' ' + current_user.middle_name + ' ' + current_user.last_name
        }
    }



    return HttpResponse(template.render(context, request))



def submitform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #counter = 0
        #chosen_number = 0
        stname = request.POST['name']
        tdate = datetime.datetime.now()

        #list
        DASS21_depression = []
        DASS21_anxiety = []
        DASS21_stress = []

        for x in request.POST.getlist('question[]'):
            objx = Question.objects.get(id=x)
            choice = request.POST[x]
            objy = Choice.objects.get(id=choice)
            #item_choose = Choice.objects.get(id=choice)
            subscaleclass_id = objx.subscaleclass_id

             # answer seperation
            if subscaleclass_id == 1 :
                #Depression
                DASS21_depression.append(objy.choice_value)
            elif subscaleclass_id == 2:
                #Anxiety
                DASS21_anxiety.append(objy.choice_value)
            else:
                #stress
                DASS21_stress.append(objy.choice_value)
            
            #saving the answer
            for_save = Answer(name_id=stname,question_id=x,answer_id=choice,date_answered=tdate)
            for_save.save()
            #counter += 1
            #chosen_number += int(choice)
        
        #dscore = chosen_number / counter
        #score_list = [getResultDepression(dscore), getResultAnxiety(dscore), getResultStress(dscore)]
        res_depress = DASS21_compute(DASS21_depression)
        res_anxiety = DASS21_compute(DASS21_anxiety)
        res_stress = DASS21_compute(DASS21_stress)
        total = res_depress + res_anxiety + res_stress
        context = {
            'results' : {
                'score' : '{:.2f}'.format(total),
                'depression' : randomForestDepression(DASS21_depression),
                'anxiety' : randomForestAnxiety(DASS21_anxiety),
                'stress' : randomForestStress(DASS21_stress)
            }
        }

        save_score = Result(
                name_id=stname,
                score = total, 
                depression= randomForestDepression(DASS21_depression),
                anxiety= randomForestAnxiety(DASS21_anxiety),
                stress= randomForestStress(DASS21_stress),
                date= tdate
                )
        save_score.save()

        #messages.success(request, 'Contact request submitted successfully.')
        template = loader.get_template('results.html')
        return HttpResponse(template.render(context, request))
        #return render(request.GET, 'form.html')
        #return HttpResponse("Saved")

    
