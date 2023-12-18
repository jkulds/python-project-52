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
        self.assertContains(response, _('nav_users'))
        self.assertContains(response, '/statuses/')
        self.assertContains(response, _('nav_statuses'))
        self.assertContains(response, '/labels/')
        self.assertContains(response, _('nav_labels'))
        self.assertContains(response, '/tasks/')
        self.assertContains(response, _('nav_tasks'))
        self.assertContains(response, '/logout/')
        self.assertContains(response, _('nav_logout'))

        self.assertNotContains(response, '/login/')
        self.assertNotContains(response, _('nav_login'))

    def test_header_nav_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('index'))

        self.assertContains(response, '/users/')
        self.assertContains(response, _('nav_users'))
        self.assertContains(response, '/login/')
        self.assertContains(response, _('nav_login'))

        self.assertNotContains(response, '/statuses/')
        self.assertNotContains(response, _('nav_statuses'))
        self.assertNotContains(response, '/labels/')
        self.assertNotContains(response, _('nav_labels'))
        self.assertNotContains(response, '/tasks/')
        self.assertNotContains(response, _('nav_tasks'))
        self.assertNotContains(response, '/logout/')
        self.assertNotContains(response, _('nav_logout'))
