from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _

from task_manager.forms import RegistrationForm, LoginForm, \
    CustomUserChangeForm, TaskStatusForm, TaskModelForm
from task_manager.models import TaskStatus, TaskModel


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
    return render(request, 'statuses/status_list.html', {'statuses': statuses})


def status_create(request):
    if request.method == 'POST':
        form = TaskStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = TaskStatusForm()
    return render(request, 'statuses/status_create.html', {'form': form})


def status_update(request, pk):
    status = get_object_or_404(TaskStatus, pk=pk)
    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = TaskStatusForm(instance=status)
    return render(request, 'statuses/status_create.html', {'form': form})


def status_delete(request, pk):
    status = get_object_or_404(TaskStatus, pk=pk)
    status.delete()
    return redirect('status_list')


def task_list(request):
    tasks = TaskModel.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assignee = User.objects.get(pk=form.data['assignee'])
            task.save()
            return redirect('task_list')
    else:
        form = TaskModelForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskModelForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)

    if request.user == task.author:
        if request.method == 'POST':
            task.delete()
            messages.success(request, _('Task deleted successfully.'))
            return redirect('task_list')
        return render(request, 'tasks/task_delete.html', {'task': task})
    else:
        messages.error(request, _('You do not have permission to delete this task.'))
        return redirect('task_list')
