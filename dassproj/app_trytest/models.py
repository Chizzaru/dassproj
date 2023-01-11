from django.db import models

from app_login.models import User

class SubscaleClass(models.Model):
    subscaleclass = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.subscaleclass)

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    subscaleclass = models.ForeignKey(SubscaleClass, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.question_text) + ' - ' + str(self.subscaleclass)
    
    '''class Meta:
        ordering = ('-id',)'''

class Choice(models.Model):
    choice_value = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.choice_value)

    
class Answer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date_answered = models.DateTimeField('date answered')

    def __str__(self):
        return str(self.question) + '? ans. ' + str(self.answer) + ' - ' + str(self.name)
    

class Result(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result')
    score = models.IntegerField(default=0)
    depression = models.CharField(max_length=200)
    anxiety = models.CharField(max_length=200)
    stress = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    def __str__(self):
        return str(self.name)