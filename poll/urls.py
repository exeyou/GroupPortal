from django.urls import path
from . import views
app_name = 'poll'

urlpatterns = [
    path('', views.poll_home, name='poll_home'),
    path('survey/<int:survey_id>/page/<int:page_order>/', views.survey_page, name='survey_page'),
    path('survey/thank-you/', views.survey_thank_you, name='survey_thank_you'),
]
