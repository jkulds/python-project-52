from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from task_manager.user.forms import CustomUserChangeForm, \
    RegistrationForm


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    success_url = reverse_lazy('users')
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/edit.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users')