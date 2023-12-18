from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext_lazy as _
from task_manager.mixins import TimeStampMixin


class TaskStatus(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True, blank=False,
                            verbose_name=_('task status name'))

    def __str__(self):
        return self.name


class LabelModel(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True, blank=False,
                            verbose_name=_('label name'))

    def __str__(self):
        return self.name


class TaskModel(TimeStampMixin):
    name = models.CharField(max_length=255, blank=False, unique=True,
                            verbose_name=_('task_name'))
    description = models.TextField(max_length=4096, blank=True,
                                   verbose_name=_('task_description'))
    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 verbose_name=_('task_executor'))
    status = models.ForeignKey(TaskStatus,
                               on_delete=models.PROTECT,
                               related_name='statuses',
                               verbose_name=_('task_status'))
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='authored_tasks',
                               verbose_name=_('task_author'))
    labels = models.ManyToManyField(LabelModel,
                                    through='TaskModelLabelModelRelation',
                                    through_fields=('task', 'label'),
                                    related_name='labels',
                                    blank=True,
                                    verbose_name=_('task_labels'))

    def __str__(self):
        return self.name


class TaskModelLabelModelRelation(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    label = models.ForeignKey(LabelModel, on_delete=models.PROTECT)
