from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_user_list_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_list.html')

    def test_user_create_view(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        # Test form submission
        data = {'username': 'newuser',
                'password': 'newpass',
                'first_name': 'test',
                'last_name': 'test2',
                'password1': 'test',
                'password2': 'test'}
        response = self.client.post(reverse('user_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(username='newuser').count(), 1)

    def test_user_update_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('user_edit', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        data = {'username': 'updateduser',
                'password': 'updateduser',
                'first_name': 'updateduser',
                'last_name': 'updateduser',
                'password1': 'updateduser',
                'password2': 'updateduser'}
        response = self.client.post(reverse('user_edit', args=[self.user.id]),
                                    data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(id=self.user.id).username,
                         'updateduser')

    def test_user_delete_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/delete.html')

        # Test deletion
        response = self.client.post(reverse('user_delete', args=[self.user.id]),
                                    {'confirm_delete': True})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(id=self.user.id).count(), 0)
