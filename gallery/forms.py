from django import forms
from .models import Media

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['file', 'description', 'media_type']
