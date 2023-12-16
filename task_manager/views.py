from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from task_manager.forms import RegistrationForm, LoginForm


def index(request):
    return render(request, 'index.html')


def users(request):
    users = User.objects.all()
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


def edit_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = RegistrationForm(instance=user)
    return render(request, 'users/edit.html', {'form': form, 'user': user})


def delete_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=400)


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