from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.poll_home, name='poll_home'),
    path('survey/<int:survey_id>/<int:question_order>/', views.survey_question, name='survey_question'),
    path('thank-you/', views.survey_thank_you, name='survey_thank_you'),
]