# admin.py
import nested_admin
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Poll, Choice, Vote
import json

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 1
    classes = ['collapse', 'choice-inline']

class PollAdmin(nested_admin.NestedModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question', 'created_at', 'updated_at', 'vote_chart']
    readonly_fields = ('vote_chart',)

    def vote_chart(self, obj):
        choices = obj.choices.all()
        if not choices.exists():
            return "No choices available."

        labels = []
        data = []

        for choice in choices:
            labels.append(choice.text)
            count = Vote.objects.filter(choice=choice).count()
            data.append(count)

        chart_id = f"vote-chart-{obj.pk}"
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
                                backgroundColor: 'rgba(255, 99, 132, 0.6)',
                                borderColor: 'rgba(255, 99, 132, 1)',
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

    vote_chart.short_description = "Vote Results Chart"

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'poll']

class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'choice', 'voted_at']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote, VoteAdmin)
