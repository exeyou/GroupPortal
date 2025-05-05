# admin.py
import nested_admin
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Survey, Question, Choice, SurveyResult, Answer
import json

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 1
    classes = ['collapse', 'choice-inline']  # Custom class for different design

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]
    show_change_link = True

class SurveyAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'created_at', 'is_active']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'survey', 'question_type', 'order', 'answer_chart']
    readonly_fields = ('answer_chart',)
    inlines = [ChoiceInline]

    def answer_chart(self, obj):
        if obj.question_type not in ['radio', 'checkbox']:
            return "No chart for text questions."

        choices = obj.choices.all()
        if not choices.exists():
            return "No choices available."

        labels = []
        data = []

        for choice in choices:
            labels.append(choice.text)
            count = Answer.objects.filter(question=obj, choices=choice).count()
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
                                label: 'Answers',
                                data: data.data,
                                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                                borderColor: 'rgba(54, 162, 235, 1)',
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

    answer_chart.short_description = "Answer Ratio Chart"

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)