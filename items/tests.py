from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Item
from users.models import User

class ItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.force_authenticate(user=self.user)
        self.create_url = reverse('item-create')
        self.item = {'name': 'Test Item', 'description': 'Test Description'}

    def test_create_item(self):
        response = self.client.post(self.create_url, self.item)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Test Item')

    def test_get_item(self):
        created_item = Item.objects.create(**self.item)
        response = self.client.get(reverse('item-detail', kwargs={'pk': created_item.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Item')

    def test_update_item(self):
        created_item = Item.objects.create(**self.item)
        response = self.client.put(reverse('item-update', kwargs={'pk': created_item.id}), {
            'name': 'Updated Item',
            'description': 'Updated Description'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Item.objects.get(id=created_item.id).name, 'Updated Item')

    def test_delete_item(self):
        created_item = Item.objects.create(**self.item)
        response = self.client.delete(reverse('item-delete', kwargs={'pk': created_item.id}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Item.objects.count(), 0)
