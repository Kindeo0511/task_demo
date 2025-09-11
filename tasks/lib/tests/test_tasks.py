from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Tasks

class TestApiTask(APITestCase):

    def setUp(self):
        self.task_data = {
            'title': 'test title',
            'description': 'test description',
            'completed': True
        }
        self.task = Tasks.objects.create(**self.task_data)
        self.list_url = reverse('task-list')
       
    
    def test_task_list(self):

        url = reverse('task-list')
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1

    def test_create_task_valid(self):
        url = reverse('task-create')
        data = {
            'title': 'New Task',
            'description': 'new description',
            'completed' : True
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == data['title']
        assert response.data['description'] == data['description']
        assert response.data['completed'] is True

    def test_create_task_invalid(self):
        url = reverse('task-create')
        data = {
            'title': '',
            'description': '',
            'completed':''
        } 
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title is required.' in response.data['title']
    
    
    def test_get_task(self):
        url = reverse('task-retrieve', kwargs={'task_id': self.task.pk})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == self.task.pk
        assert response.data['title'] == self.task.title
        assert response.data['description'] == self.task.description
        assert response.data['completed'] == self.task.completed
    
    def test_get_task_not_found(self):
        url = reverse('task-retrieve', kwargs={'task_id': 9999})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_task_valid(self):
        url = reverse('task-update', kwargs={'task_id': self.task.pk})
        data = {
        "title": "Updated Task",
        "description": "Updated via test",
        "completed": True
    }
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == data['title']
        assert response.data['description'] == data['description']
        assert response.data['completed'] is True
    
    def test_update_task_partial(self):
        url = reverse('task-update', kwargs={'task_id': self.task.pk})
        data = {
            'title': 'partial task'
        }
        response = self.client.patch(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == data['title']

    def test_update_task_invalid(self):
        url = reverse ('task-update', kwargs={'task_id': self.task.pk})
        data = {
            'title': '',
            'description': 'updated desc',
            'completed': True
        }
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title is required.' in response.data['title']

    def test_delete_task(self):
        url = reverse('task-delete', kwargs={'task_id': self.task.pk})
        
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Tasks.objects.count() == 0
    
    def test_delete_task_not_found(self):
        url = reverse('task-delete', kwargs={'task_id': 9999})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

        





