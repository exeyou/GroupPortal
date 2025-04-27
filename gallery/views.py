from django.shortcuts import render, redirect
from .forms import MediaForm
from .models import Media
from django.contrib.auth.decorators import login_required, user_passes_test

def media_gallery(request):
    media_files = Media.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'gallery/gallery.html', {'media_files': media_files})


@login_required
def upload_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.user = request.user
            media.save()  # Зберігається, але ще не approved
            return redirect('gallery:media_gallery')
    else:
        form = MediaForm()
    return render(request, 'gallery/upload.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def moderate_media(request):
    media_files = Media.objects.filter(is_approved=False)
    return render(request, 'gallery/moderate.html', {'media_files': media_files})

@user_passes_test(lambda u: u.is_staff)
def approve_media(request, media_id):
    media = Media.objects.get(id=media_id)
    media.is_approved = True
    media.save()
    return redirect('gallery:moderate_media')
