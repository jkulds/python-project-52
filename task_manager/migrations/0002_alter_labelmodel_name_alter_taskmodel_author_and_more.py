# Generated by Django 4.2.8 on 2023-12-20 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelmodel',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authored_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.TextField(blank=True, max_length=4096, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='executor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='task_manager.TaskModelLabelModelRelation', to='task_manager.labelmodel', verbose_name='Метки'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='task_name'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='task_manager.taskstatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя'),
        ),
    ]
