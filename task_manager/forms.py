from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DetailView, \
    DeleteView

from task_manager.models import TaskStatus, TaskModel


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 help_text=_('required'))
    last_name = forms.CharField(max_length=30,
                                required=True,
                                help_text=_('required'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text=_('required'))
    last_name = forms.CharField(max_length=30, required=True,
                                help_text=_('required'))
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=_('Enter password'))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                help_text=_('Confirm password'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password',
                  'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = _(
            'Enter new password')
        self.fields['password2'].widget.attrs['placeholder'] = _(
            'Confirm password')


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ['name']


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'assignee', 'status']


class TaskModelCreateView(CreateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskModelUpdateView(UpdateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'tasks/task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskModelListView(ListView):
    model = TaskModel
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskModelDetailView(DetailView):
    model = TaskModel
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskModelDeleteView(DeleteView):
    model = TaskModel
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
