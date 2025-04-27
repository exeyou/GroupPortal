
from django.contrib import admin
from .models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('description', 'media_type', 'is_approved',)
    list_filter = ('is_approved', 'media_type',)
    search_fields = ('description',)


@admin.action(description="available")
def Available(self, request, queryset):
    queryset.update(is_approved = "True")