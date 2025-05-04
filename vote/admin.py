from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.response import TemplateResponse
from django.urls import path

from .models import Poll, Choice, Vote

class PollAdmin(admin.ModelAdmin):
    change_form_template = 'admin/vote/vote_detail.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        poll = Poll.objects.get(pk=object_id)
        choices = poll.choices.all()
        vote_data = []

        for choice in choices:
            count = Vote.objects.filter(poll=poll, choice=choice).count()
            vote_data.append({'label': choice.text, 'count': count})

        extra_context = extra_context or {}
        extra_context['vote_data'] = vote_data
        extra_context['poll'] = poll

        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )

admin.site.register(Poll, PollAdmin)
