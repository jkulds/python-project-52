from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import LabelForm
from ..models import LabelModel


class LabelListView(ListView):
    model = LabelModel
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'


class LabelCreateView(CreateView):
    model = LabelModel
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('label_list')
    context_object_name = 'label'


class LabelUpdateView(UpdateView):
    model = LabelModel
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('label_list')
    context_object_name = 'label'


class LabelDeleteView(DeleteView):
    model = LabelModel
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('label_list')
    context_object_name = 'label'
