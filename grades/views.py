from django.shortcuts import render, redirect, get_object_or_404
from .forms import GradeForm
from .models import Grade
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_staff

@login_required
def grade_list(request):
    show_user_grades = request.GET.get('show_user_grades') == 'on'
    grades = Grade.objects.all()

    if show_user_grades:
        grades = grades.filter(student=request.user)

    return render(request, 'grades/grades_list.html', {'grades': grades, 'show_user_grades': show_user_grades})

@user_passes_test(is_admin)
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades:grade_list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_form.html', {'form': form})

@user_passes_test(is_admin)
def edit_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades:grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form})

@user_passes_test(is_admin)
def delete_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grades:grade_list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})
