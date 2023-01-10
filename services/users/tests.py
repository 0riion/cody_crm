from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import User
from .serializers import UserSerializer


class UserViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse('users-list')
        self.detail_url = reverse('users-detail', args=[1])
        self.user_data = {'username': 'testuser',
                          'email': 'test@example.com', 'password': 'testpass'}
        self.response = self.client.post(
            self.list_url, self.user_data, format='json')
        self.user = User.objects.get(id=1)

    def test_list(self):
        response = self.client.get(self.list_url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(
            self.response.data['username'], self.user_data['username'])
        self.assertEqual(self.response.data['email'], self.user_data['email'])

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        user = User.objects.get(pk=1)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        update_data = {'username': 'newusername', 'email': 'new@example.com'}
        response = self.client.put(self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], update_data['username'])
        self.assertEqual(response.data['email'], update_data['email'])

    def test_partial_update(self):
        update_data = {'username': 'newusername'}
        response = self.client.patch(
            self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], update_data['username'])

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), 0)
