from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class IndexTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_index_view(self):
        response = self.client.get(reverse_lazy('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='index.html')
        self.assertContains(response, _('ToDo app'), status_code=200)

    def test_header_nav_logged_in(self):
        response = self.client.get(reverse_lazy('index'))

        self.assertContains(response, '/users/')
        self.assertContains(response, _('Пользователи'))
        self.assertContains(response, '/statuses/')
        self.assertContains(response, _('Статусы'))
        self.assertContains(response, '/labels/')
        self.assertContains(response, _('Метки'))
        self.assertContains(response, '/tasks/')
        self.assertContains(response, _('Задачи'))
        self.assertContains(response, '/logout/')
        self.assertContains(response, _('Выход'))

        self.assertNotContains(response, '/login/')
        self.assertNotContains(response, _('Вход'))

    def test_header_nav_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('index'))

        self.assertContains(response, '/users/')
        self.assertContains(response, _('Пользователи'))
        self.assertContains(response, '/login/')
        self.assertContains(response, _('Вход'))

        self.assertNotContains(response, '/statuses/')
        self.assertNotContains(response, _('Статусы'))
        self.assertNotContains(response, '/labels/')
        self.assertNotContains(response, _('Метки'))
        self.assertNotContains(response, '/tasks/')
        self.assertNotContains(response, _('Задачи'))
        self.assertNotContains(response, '/logout/')
        self.assertNotContains(response, _('Выход'))
