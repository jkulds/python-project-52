from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.models import TaskStatus
from task_manager.status.forms import TaskStatusForm


class StatusListView(ListView):
    model = TaskStatus
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    model = TaskStatus
    form_class = TaskStatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('status_list')


class StatusUpdateView(UpdateView):
    model = TaskStatus
    form_class = TaskStatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('status_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TaskStatus, pk=pk)


class StatusDeleteView(DeleteView):
    model = TaskStatus
    template_name = 'status/status_delete.html'
    success_url = reverse_lazy('status_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TaskStatus, pk=pk)
