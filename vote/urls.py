from django.urls import path
from . import views

app_name = 'vote'

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
]
