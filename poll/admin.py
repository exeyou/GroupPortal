from django.contrib import admin
from .models import Survey, SurveyPage, Question, Choice, SurveyResult, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class SurveyPageInline(admin.StackedInline):
    model = SurveyPage
    extra = 1

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [SurveyPageInline]

@admin.register(SurveyPage)
class SurveyPageAdmin(admin.ModelAdmin):
    list_display = ['survey', 'order']
    ordering = ['survey', 'order']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(SurveyResult)
admin.site.register(Answer)
