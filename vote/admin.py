from django.contrib import admin
from .models import Poll, Choice, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote)

