from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
    path('calendar', views.calendar_view, name='calendar'),
    path('event_detail/<int:event_id>/', views.event_view, name='event_detail'),
]