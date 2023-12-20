from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from .forms import LabelForm
from ..mixins import AuthMixin, DeleteOwnMixin
from ..models import LabelModel


class LabelListView(AuthMixin, ListView):
    model = LabelModel
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'
    extra_context = {
        'btn_text': _('Создать метку'),
        'title': _('Метки')
    }


class LabelCreateView(AuthMixin, SuccessMessageMixin, CreateView):
    model = LabelModel
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('label_list')
    success_message = _('Метка успешно создана')
    context_object_name = 'label'
    extra_context = {
        'btn_text': _('Создать'),
        'title': _('Создать метку')
    }


class LabelUpdateView(AuthMixin, SuccessMessageMixin, UpdateView):
    model = LabelModel
    form_class = LabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('label_list')
    success_message = _('Метка успешно изменена')
    context_object_name = 'label'
    extra_context = {
        'btn_text': _('Изменить '),
        'title': _('Изменить метку')
    }


class LabelDeleteView(AuthMixin, SuccessMessageMixin,
                      DeleteOwnMixin, DeleteView):
    model = LabelModel
    template_name = 'delete_form.html'
    success_url = reverse_lazy('label_list')
    success_message = _('Метка успешно удалена')
    context_object_name = 'object'
    protected_message = _("cant delete label because of using"),
    protected_url = reverse_lazy('label_list')
    extra_context = {
        'btn_text': _('Да, удалить'),
        'title': _('Удалить метку')
    }
