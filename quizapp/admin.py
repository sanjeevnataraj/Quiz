from django.contrib import admin
from .models import Questions,User,QuestionChoices,UserQuestionAnswers
# Register your models here.
admin.site.register(User)
admin.site.register(Questions)
admin.site.register(QuestionChoices)
admin.site.register(UserQuestionAnswers)

