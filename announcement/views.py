from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Announcement
from .forms import AnnouncementForm

# Функція для перевірки прав доступу
def is_admin_or_moderator(user):
    return user.is_superuser or user.groups.filter(name__in=['moderator']).exists()

# Виведення списку оголошень (доступно всім)
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcement/announcement_list.html', {'announcements': announcements})

# Створення оголошення (лише для адмінів або модераторів)
@user_passes_test(is_admin_or_moderator)
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements:announcement_list')
    else:
        form = AnnouncementForm()
    return render(request, 'announcement/announcement_form.html', {'form': form})

# Редагування оголошення (лише для адмінів або модераторів)
@user_passes_test(is_admin_or_moderator)
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcements:announcement_list')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcement/announcement_form.html', {'form': form})

# Видалення оголошення (лише для адмінів або модераторів)
@user_passes_test(is_admin_or_moderator)
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcements:announcement_list')
    return render(request, 'announcement/confirm_delete.html', {'announcement': announcement})

# Create your views here.
