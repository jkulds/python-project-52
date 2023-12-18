from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import LabelModel


class LabelModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.label = LabelModel.objects.create(name='Test Label')

    def test_label_list_view(self):
        response = self.client.get(reverse('label_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_list.html')
        self.assertContains(response, 'Test Label')

    def test_label_create_view(self):
        response = self.client.post(reverse('label_create'),
                                    {'name': 'New Label'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(LabelModel.objects.filter(name='New Label').exists())

    def test_label_update_view(self):
        response = self.client.post(reverse('label_update',
                                            args=[self.label.id]),
                                    {'name': 'Updated Label'})
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Updated Label')

    def test_label_delete_view(self):
        response = self.client.post(reverse('label_delete',
                                            args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(LabelModel.objects.filter(name='Test Label').exists())

    def test_label_create_view_with_invalid_data(self):
        response = self.client.post(reverse('label_create'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Обязательное поле')

    def test_label_update_view_with_invalid_id(self):
        response = self.client.post(reverse('label_update', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_label_delete_view_with_invalid_id(self):
        response = self.client.post(reverse('label_delete', args=[999]))
        self.assertEqual(response.status_code, 404)
