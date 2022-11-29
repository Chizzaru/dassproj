from django import forms
from .models import Question, Choice


class DassForm(forms.Form):
    myQuestions = Question.objects.all().values()
    myChoices = Choice.objects.all().values()


    
    for x in myQuestions:
        question = forms.CharField(
                label=x.question_text,max_length=200,
                widget=forms.TextInput(attrs={'type':'hidden','class':'form-control','name':'question[]'}))
        

        

