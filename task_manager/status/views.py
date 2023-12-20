from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import DeleteOwnMixin, AuthMixin
from task_manager.models import TaskStatus
from task_manager.status.forms import TaskStatusForm


class StatusListView(AuthMixin, ListView):
    model = TaskStatus
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Статусы'),
        'btn_text': _('Создать статус'),
    }


class StatusCreateView(AuthMixin, SuccessMessageMixin, CreateView):
    model = TaskStatus
    form_class = TaskStatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Статус успешно создан')
    extra_context = {
        'btn_text': _('Создать'),
        'title': _('Создать статус')
    }


class StatusUpdateView(AuthMixin, SuccessMessageMixin, UpdateView):
    model = TaskStatus
    form_class = TaskStatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Статус успешно изменен')
    extra_context = {
        'btn_text': _('Изменить'),
        'title': _('Изменить статус')
    }

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TaskStatus, pk=pk)


class StatusDeleteView(AuthMixin, SuccessMessageMixin, DeleteOwnMixin,
                       DeleteView):
    model = TaskStatus
    template_name = 'delete_form.html'
    success_url = reverse_lazy('status_list')
    success_message = _('Статус успешно удален')
    context_object_name = 'object'
    protected_message = _("cant delete status because of using"),
    protected_url = reverse_lazy('status_list')
    extra_context = {
        'btn_text': _('Да, удалить'),
        'title': _('Удалить статус')
    }

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TaskStatus, pk=pk)
