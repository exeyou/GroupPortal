import nested_admin
from .models import Survey, SurveyPage, Question, Choice, SurveyResult, Answer
from django.contrib import admin

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 2

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class SurveyPageInline(nested_admin.NestedStackedInline):
    model = SurveyPage
    extra = 1
    inlines = [QuestionInline]

@admin.register(Survey)
class SurveyAdmin(nested_admin.NestedModelAdmin):
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
