from django.urls import path
from tasks.lib.api.views import TaskList, TaskCreate, TaskGetById, TaskDelete, TaskUpdate
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/create', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:task_id>/', TaskGetById.as_view(), name='task-retrieve'),
    path('tasks/update/<int:task_id>/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:task_id>/', TaskDelete.as_view(), name='task-delete'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]