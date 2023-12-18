from django import forms

from task_manager.models import TaskModel


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['name', 'description', 'executor', 'status', 'labels']
