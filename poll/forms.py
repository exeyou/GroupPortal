from django import forms
from .models import Answer, Choice, Question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'text_answer', 'choices']


class DynamicSurveyForm(forms.Form):
    # Створіть динамічні поля для кожного питання
    def __init__(self, *args, **kwargs):
        survey = kwargs.pop('survey', None)  # Отримуємо об'єкт опитування
        super(DynamicSurveyForm, self).__init__(*args, **kwargs)

        if survey:
            for question in survey.questions.all():
                if question.question_type == 'text':
                    self.fields[f'question_{question.id}'] = forms.CharField(label=question.text, required=False)
                elif question.question_type == 'radio':
                    choices = [(choice.id, choice.text) for choice in question.choices.all()]
                    self.fields[f'question_{question.id}'] = forms.ChoiceField(label=question.text, choices=choices, widget=forms.RadioSelect)
                elif question.question_type == 'checkbox':
                    choices = [(choice.id, choice.text) for choice in question.choices.all()]
                    self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(label=question.text, choices=choices, widget=forms.CheckboxSelectMultiple)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['page', 'text', 'question_type']