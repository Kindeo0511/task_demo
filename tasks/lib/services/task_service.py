from tasks.models import Tasks
from django.shortcuts import get_object_or_404

def get_all_tasks():
    return Tasks.objects.all()

def get_task_by_id(pk):
    return get_object_or_404(Tasks, pk=pk)

def create_task(data):
    return Tasks.objects.create(**data)

def update_task(task, data):
    for field, value in data.items():
        setattr(task, field, value)
    task.save()
    return task

def delete_task(task):
    task.delete()
