from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.test import Client

from task_manager.models import TaskModel, TaskStatus


class TaskCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.status = TaskStatus.objects.create(name="Test Status")
        self.task = TaskModel.objects.create(title='Test Task',
                                             description='Test Description',
                                             assignee=self.user,
                                             status=self.status,
                                             author=self.user)
        self.client = Client()

    def test_task_create(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('task_create')
        response = self.client.post(url, {'title': 'New Task',
                                          'description': 'New Description',
                                          'assignee': self.user.id,
                                          'status': self.status})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(TaskModel.objects.filter(title='New Task').exists())

    def test_task_update(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('task_update', args=[self.task.id])
        response = self.client.post(url, {'title': 'Updated Task',
                                          'description': 'Updated Description',
                                          'assignee': self.user.id,
                                          'status': self.status})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_detail(self):
        url = reverse('task_detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_task_delete(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('task_delete', args=[self.task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TaskModel.objects.filter(title='Test Task').exists())

    def tearDown(self):
        self.client.logout()
