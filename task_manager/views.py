from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from task_manager.forms import RegistrationForm, LoginForm, \
    CustomUserChangeForm
from task_manager.models import TaskStatus


def index(request):
    return render(request, 'index.html')


def users(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def users_create(request):
    return render(request, 'users/user_list.html', {'users': users})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def edit_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            return render(request, 'users/edit.html', {'form': form, 'user': user})
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/edit.html', {'form': form, 'user': user})


def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')

    return render(request, 'users/delete.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def status_list(request):
    statuses = TaskStatus.objects.all()
    return render(request, 'status_list.html', {'statuses': statuses})


def status_detail(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    return render(request, 'status_detail.html', {'status': status})


def status_create(request):
    if request.method == 'POST':
        form = TaskStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = TaskStatusForm()
    return render(request, 'status_form.html', {'form': form})

def status_update(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = TaskStatusForm(instance=status)
    return render(request, 'status_form.html', {'form': form})

def status_delete(request, status_id):
    status = get_object_or_404(TaskStatus, pk=status_id)
    status.delete()
    return redirect('status_list')