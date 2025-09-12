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
        self.create_url = reverse('task-create')
        self.update_url = reverse('task-update', kwargs={'task_id': self.task.pk})
   
       
           
    def get_task_payload(self, title = 'new task', description = "new description", completed = True):

        return {
            'title': title,
            'description': description,
            'completed': completed 
        }
    
    def test_task_list(self):

        response = self.client.get(self.list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1

  
    def test_create_task_valid(self):

        data = self.get_task_payload()
        response = self.client.post(self.create_url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == data['title']
        assert response.data['description'] == data['description']
        assert response.data['completed'] is True

    def test_create_task_missing_field(self):
        data = {
            'description': 'invalid description',
            'completed': True
        }
        response = self.client.post(self.create_url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title is required.' in response.data['title']
    
    def test_create_task_blank_field(self):
        data = {
            'title': '',
            'description': 'invalid description',
            'completed': True
        }
        response = self.client.post(self.create_url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title cannot be blank.' in response.data['title']
    
    
    
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
     
        data = self.get_task_payload(title='updated task', description='updated description', completed= True)

        response = self.client.put(self.update_url, data, format='json')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == data['title']
        assert response.data['description'] == data['description']
        assert response.data['completed'] is True
    
    def test_update_task_blank_field(self):

        data = {
            'title': '',
            'description': 'invalid description',
            'completed': True
        }

        response = self.client.put(self.update_url, data, format='json')
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title cannot be blank.' in response.data['title']
    
    def test_update_task_missing_field(self):

        data = {        
            'description': 'invalid description',
            'completed': True
        }
        response = self.client.put(self.update_url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title is required.' in response.data['title']

    def test_update_task_partial(self):
 
        data = self.get_task_payload(title= 'updated title via partial')

        response = self.client.patch(self.update_url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == data['title']
    
    def test_update_task_partial_blank_field(self):
         
        data = {
            'title': '',
            'description': '',
            'completed': True
        }

        response = self.client.patch(self.update_url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'Title cannot be blank.' in response.data['title']
        assert 'description' in response.data
        assert 'Description cannot be blank' in response.data['description']




    def test_delete_task(self):
        url = reverse('task-delete', kwargs={'task_id': self.task.pk})
        
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Tasks.objects.count() == 0
    
    def test_delete_task_not_found(self):
        url = reverse('task-delete', kwargs={'task_id': 9999})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

 
 






