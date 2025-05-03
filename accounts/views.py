from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.timezone import now, timedelta
from django.views import View
from django.views.generic import ListView, TemplateView
from .forms import RegisterForm, LoginForm, ProjectForm, UserUpdateForm, GradeForm
from .models import PortfolioProject, Grade


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'accounts/register_page.html', {'form':form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            print('registered')
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register_page.html", {"form":form})


from django.contrib import messages


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'accounts/login_page.html', {'form': form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Неправильное имя пользователя или пароль.")

        return render(request, "accounts/login_page.html", {"form": form})
    return None


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def my_portfolio(request):
    projects = request.user.projects.all()
    return render(request, 'accounts/portfolio_list.html', {'projects': projects})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('accounts:my_portfolio')
    else:
        form = ProjectForm()
    return render(request, 'accounts/project_form.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(PortfolioProject, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('accounts:my_portfolio')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'accounts/project_form.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(PortfolioProject, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('accounts:my_portfolio')
    return render(request, 'accounts/project_confirm_delete.html', {'project': project})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  # Назва урла
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile_edit.html', {'form': form})


def is_admin(user):
    return user.is_staff

@login_required
def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grades/grades_list.html', {'grades': grades})

@user_passes_test(is_admin)
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
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
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form})

@user_passes_test(is_admin)
def delete_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})
