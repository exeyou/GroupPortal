
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Event
import json

def calendar_view(request):
    events = Event.objects.all()
    events_data = [
        {
            'title': event.name,
            'start': event.date.strftime('%Y-%m-%dT%H:%M:%S'),
            'url': f'/events/event_detail/{event.id}/',  # Link to detail page
        }
        for event in events
    ]
    return render(request, 'events/calendar.html', {'events_json': json.dumps(events_data)})


def event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})