from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from task_manager.models import TaskModel, TaskStatus


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.status = TaskStatus.objects.create(name="test status")
        self.task = TaskModel.objects.create(name='Test Task',
                                             author=self.user,
                                             status=self.status,
                                             executor=self.user)

    def test_task_model_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_list.html')
        self.assertContains(response, 'Test Task')

    def test_task_model_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_detail.html')
        self.assertContains(response, 'Test Task')

    def test_task_model_create_view(self):
        response = self.client.post(reverse('task_create'),
                                    {'name': 'New Task',
                                     'executor': self.user.id,
                                     'status': self.status.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(TaskModel.objects.filter(name='New Task').exists())

    def test_task_model_update_view(self):
        response = self.client.post(reverse('task_update',
                                            args=[self.task.id]),
                                    {'name': 'Updated Task',
                                     'executor': self.user.id,
                                     'status': self.status.id})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')

    def test_task_model_delete_view(self):
        response = self.client.post(reverse('task_delete',
                                            args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TaskModel.objects.filter(name='Test Task').exists())

    def test_task_model_create_view_with_invalid_data(self):
        response = self.client.post(reverse('task_create'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Обязательное поле')

    def test_task_model_update_view_with_invalid_id(self):
        response = self.client.post(reverse('task_update', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_task_model_delete_view_with_invalid_id(self):
        response = self.client.post(reverse('task_delete', args=[999]))
        self.assertEqual(response.status_code, 404)
