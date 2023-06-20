# from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class BlankViewTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='admin123')

    def test_blank_view_superuser(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('blank'))
        self.assertEqual(response.status_code, 200, msg='Expected status code 200 for superuser')
        self.assertTemplateUsed(response, 'blank.html', msg_prefix='Superuser should see the blank.html template')

    def test_blank_view_non_superuser(self):
        user = User.objects.create_user(username='user', password='password')
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('blank'))
        self.assertRedirects(response, reverse('login'), msg_prefix='Non-superuser should be redirected to login')
        self.assertEqual(response.status_code, 302, msg='Expected status code 302 for non-superuser redirect')
