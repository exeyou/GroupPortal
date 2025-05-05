from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.response import TemplateResponse
from django.urls import path

from .models import Poll, Choice, Vote

from django.utils.safestring import mark_safe
import json

class PollAdmin(admin.ModelAdmin):
    readonly_fields = ('vote_chart',)  # <- add a read-only field for the chart

    def change_view(self, request, object_id, form_url='', extra_context=None):
        poll = Poll.objects.get(pk=object_id)
        choices = poll.choices.all()
        vote_data = []

        for choice in choices:
            count = Vote.objects.filter(poll=poll, choice=choice).count()
            vote_data.append({'label': choice.text, 'count': count})

        chart_labels = [item['label'] for item in vote_data]
        chart_data = [item['count'] for item in vote_data]

        extra_context = extra_context or {}
        extra_context['vote_labels'] = json.dumps(chart_labels)
        extra_context['vote_counts'] = json.dumps(chart_data)
        extra_context['poll'] = poll

        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )

    def vote_chart(self, obj):
        choices = obj.choices.all()
        if not choices.exists():
            return "No choices available."

        labels = []
        data = []

        for choice in choices:
            labels.append(choice.text)
            count = Vote.objects.filter(poll=obj, choice=choice).count()
            data.append(count)

        chart_id = f"chart-{obj.pk}"
        chart_data = json.dumps({
            'labels': labels,
            'data': data,
        })

        return mark_safe(f"""
            <canvas id="{chart_id}" width="400" height="200"></canvas>
            <script>
                (function() {{
                    var ctx = document.getElementById('{chart_id}').getContext('2d');
                    var data = {chart_data};
                    new Chart(ctx, {{
                        type: 'bar',
                        data: {{
                            labels: data.labels,
                            datasets: [{{
                                label: 'Votes',
                                data: data.data,
                                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                                borderColor: 'rgba(75, 192, 192, 1)',
                                borderWidth: 1
                            }}]
                        }},
                        options: {{
                            scales: {{
                                y: {{
                                    beginAtZero: true
                                }}
                            }}
                        }}
                    }});
                }})();
            </script>
        """)

    vote_chart.short_description = "Vote Chart"

admin.site.register(Poll, PollAdmin)
