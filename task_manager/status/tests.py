from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import TaskStatus


class StatusTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.status = TaskStatus.objects.create(name='Test Status')

    def test_status_list_view(self):
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'status/status_list.html')
        self.assertContains(response, 'Test Status')

    def test_status_create_view(self):
        response = self.client.post(reverse('status_create'),
                                    {'name': 'New Status'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(TaskStatus.objects.filter(name='New Status').exists())

    def test_status_update_view(self):
        response = self.client.post(
            reverse('status_update', args=[self.status.id]),
            {'name': 'Updated Status'})
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Updated Status')

    def test_status_delete_view(self):
        response = self.client.post(
            reverse('status_delete', args=[self.status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            TaskStatus.objects.filter(name='Test Status').exists())

    def test_status_update_view_with_invalid_id(self):
        # Test updating with an invalid ID, should return 404
        response = self.client.post(reverse('status_update', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_status_delete_view_with_invalid_id(self):
        # Test deleting with an invalid ID, should return 404
        response = self.client.post(reverse('status_delete', args=[999]))
        self.assertEqual(response.status_code, 404)
