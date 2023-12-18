from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from task_manager.user.forms import UserEditForm


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    success_url = reverse_lazy('users')
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserEditForm
    success_url = reverse_lazy('/')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'form.html'
    form_class = UserEditForm
    success_url = reverse_lazy('/')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users')
