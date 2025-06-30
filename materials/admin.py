from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    readonly_fields = ('display_youtube_video_id',)

    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def display_youtube_video_id(self, obj):
        return obj.youtube_video_id
    display_youtube_video_id.short_description = 'YouTube Video ID'
