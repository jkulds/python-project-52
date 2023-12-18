from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, \
    DeleteView
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import DeleteOwnMixin, AuthMixin
from task_manager.models import TaskModel
from task_manager.task.filters import TaskModelFilter
from task_manager.task.forms import TaskModelForm


class TaskModelCreateView(AuthMixin, SuccessMessageMixin, CreateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'title': _('create task')
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskModelUpdateView(AuthMixin, SuccessMessageMixin, UpdateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'btn_text': _('update'),
        'title': _('update task')
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskModelListView(AuthMixin, FilterView):
    model = TaskModel
    filterset_class = TaskModelFilter.TaskModelFilter
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': _('task list')
    }


class TaskModelDetailView(AuthMixin, SuccessMessageMixin, DetailView):
    model = TaskModel
    template_name = 'task/task_detail.html'
    context_object_name = 'task'
    extra_context = {
        'title': _('task detail')
    }


class TaskModelDeleteView(AuthMixin, SuccessMessageMixin, DeleteOwnMixin,
                          DeleteView):
    model = TaskModel
    template_name = 'task/task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'btn_text': _('delete'),
        'title': _('delete task?')
    }
