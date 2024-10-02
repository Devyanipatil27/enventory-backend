from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')

    def test_register_user(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login_user(self):
        # First register the user
        self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        
        # Now login with the same credentials
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
