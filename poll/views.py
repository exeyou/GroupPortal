# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Question, SurveyResult, Answer

from django.contrib.auth.decorators import login_required

def poll_home(request):
    surveys = Survey.objects.filter(is_active=True)
    return render(request, 'poll/home.html', {'surveys': surveys})

def survey_thank_you(request):
    return render(request, 'poll/survey_thank_you.html')

@login_required
def survey_question(request, survey_id, question_order):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.order_by('order')  # FIXED here!
    question_list = list(questions)

    if question_order < 1 or question_order > len(question_list):
        return redirect('poll:survey_thank_you')

    current_question = question_list[question_order - 1]

    if request.method == 'POST':
        survey_result, created = SurveyResult.objects.get_or_create(user=request.user, survey=survey)

        if current_question.question_type in ['radio', 'checkbox']:
            selected_choices = request.POST.getlist(f"question_{current_question.id}")
            if selected_choices:
                answer = Answer.objects.create(result=survey_result, question=current_question)
                answer.choices.set(selected_choices)
        else:
            text = request.POST.get(f"question_{current_question.id}", '')
            if text:
                Answer.objects.create(result=survey_result, question=current_question, text_answer=text)

        if question_order < len(question_list):
            return redirect('poll:survey_question', survey_id=survey.id, question_order=question_order + 1)
        else:
            return redirect('poll:survey_thank_you')

    return render(request, 'poll/survey_page.html', {
        'survey': survey,
        'question': current_question,
        'question_order': question_order,
        'total_questions': len(question_list),
    })
