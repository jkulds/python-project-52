from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import UserPermissionMixin, AuthMixin, DeleteOwnMixin
from task_manager.user.forms import UserEditForm


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    success_url = reverse_lazy('users')
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserEditForm
    success_message = _('Пользователь успешно зарегистрирован')
    success_url = reverse_lazy('login')
    extra_context = {
        'title': _('Регистрация'),
        'btn_text': _('Зарегистрировать')
    }


class UserUpdateView(AuthMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'form.html'
    form_class = UserEditForm
    success_url = reverse_lazy('users')
    success_message = _('Пользователь успешно изменен')
    permission_message = _('У вас нет прав для изменения другого пользователя')
    permission_url = reverse_lazy('users')
    extra_context = {
        'btn_text': _('Изменить'),
        'title': _('Изменение пользователя')
    }


class UserDeleteView(AuthMixin, UserPermissionMixin,
                     DeleteOwnMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('Пользователь успешно удален')
    protected_message = _("Невозможно удалить, т.к. элемент используется"),
    protected_url = reverse_lazy('users')
    permission_message = _('У вас нет прав для изменения другого пользователя')
    permission_url = reverse_lazy('users')
    extra_context = {
        'btn_text': _('Да, удалить'),
        'title': _('Удаление пользовавтеля')
    }
