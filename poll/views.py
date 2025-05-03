# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, SurveyPage, Question, SurveyResult, Answer, Choice
from .forms import DynamicSurveyForm
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm


def poll_home(request):
    surveys = Survey.objects.filter(is_active=True)
    return render(request, 'poll/home.html', {'surveys': surveys})

def survey_thank_you(request):
    return render(request, 'poll/survey_thank_you.html')


def survey_page(request, survey_id, page_order):
    survey = Survey.objects.get(id=survey_id)
    page = survey.pages.get(order=page_order)
    questions = page.questions.all()

    if request.method == 'POST':
        survey_result, created = SurveyResult.objects.get_or_create(user=request.user, survey=survey)

        for question in questions:
            answer_text = request.POST.get(f"question_{question.id}")
            if question.question_type == 'radio' or question.question_type == 'checkbox':
                choices = request.POST.getlist(f"question_{question.id}")
                answer = Answer.objects.create(result=survey_result, question=question)
                answer.choices.set(choices)
                answer.save()
            elif question.question_type == 'text':
                answer = Answer.objects.create(result=survey_result, question=question, text_answer=answer_text)
                answer.save()

        return redirect('poll:survey_thank_you')

    return render(request, 'poll/survey_page.html', {
        'survey': survey,
        'page': page,
        'questions': questions,
    })


@login_required
def survey_done(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    return render(request, 'survey_page.html', {'survey': survey})


