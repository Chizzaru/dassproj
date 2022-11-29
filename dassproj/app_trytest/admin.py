from django.contrib import admin
from .models import Choice, Question, Answer, Result, SubscaleClass


admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(SubscaleClass)