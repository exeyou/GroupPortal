from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Question, SurveyResult, Answer

from django.contrib.auth.decorators import login_required
from django.db.models import Count

def poll_home(request):
    surveys = Survey.objects.filter(is_active=True)

    surveys_completed_once = []
    if request.user.is_authenticated:
        completed_surveys = SurveyResult.objects.filter(user=request.user).values('survey').annotate(count=Count('id'))
        surveys_completed_once = [item['survey'] for item in completed_surveys if item['count'] == 1]
        completed_twice_ids = [item['survey'] for item in completed_surveys if item['count'] >= 2]
        surveys = surveys.exclude(id__in=completed_twice_ids)

    return render(request, 'poll/home.html', {
        'surveys': surveys,
        'surveys_completed_once': surveys_completed_once,
    })

def survey_thank_you(request):
    return render(request, 'poll/survey_thank_you.html')

@login_required
def survey_question(request, survey_id, question_order):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.order_by('order')
    question_list = list(questions)

    if question_order < 1 or question_order > len(question_list):
        return redirect('poll:survey_thank_you')

    current_question = question_list[question_order - 1]

    # Check how many attempts already exist
    attempts = SurveyResult.objects.filter(user=request.user, survey=survey).count()
    if attempts >= 2:
        return redirect('poll:survey_thank_you')

    if request.method == 'POST':
        # Create or get SurveyResult for current attempt
        survey_result, created = SurveyResult.objects.get_or_create(user=request.user, survey=survey, attempt=attempts + 1)

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
