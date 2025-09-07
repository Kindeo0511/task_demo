from django.urls import path
from tasks.lib.api.views import TaskList, TaskCreate, TaskGetById, TaskDelete, TaskUpdate

urlpatterns = [
    
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/create', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskGetById.as_view(), name='task-retrieve'),
    path('tasks/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')

]