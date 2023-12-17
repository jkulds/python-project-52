from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, \
    DeleteView

from task_manager.models import TaskModel
from task_manager.task.forms import TaskModelForm


class TaskModelCreateView(CreateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskModelUpdateView(UpdateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskModelListView(ListView):
    model = TaskModel
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'


class TaskModelDetailView(DetailView):
    model = TaskModel
    template_name = 'task/task_detail.html'
    context_object_name = 'task'


class TaskModelDeleteView(DeleteView):
    model = TaskModel
    template_name = 'task/task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
