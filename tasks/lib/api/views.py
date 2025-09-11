from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from tasks.lib.serializers.serializer import TaskSerializer
from django.shortcuts import get_object_or_404
from tasks.lib.services.task_service import (get_all_tasks, get_task_by_id, create_task, update_task, delete_task)

from tasks.models import Tasks


class TaskList(APIView):
    
    def get(self, request: Request) -> Response:
        tasks = get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskCreate(APIView):

    def post(self, request: Request) -> Response:
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            task = create_task(serializer.validated_data)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskGetById(APIView):
    def get (self, request, task_id: int) -> Response:
        task = get_task_by_id(task_id)
        serializer = TaskSerializer(task)
        return Response (serializer.data, status=status.HTTP_200_OK)

class TaskUpdate(APIView):
    def put(self, request, task_id: int) -> Response:
        task = get_task_by_id(task_id)
        serializer =TaskSerializer(task, data= request.data, partial= True)
        if(serializer.is_valid()):
            update = update_task(task, serializer.validated_data)
            return Response(TaskSerializer(update).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, task_id: int) -> Response:
        task = get_task_by_id(task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            update = update_task(task, serializer.validated_data)
            return Response(TaskSerializer(update).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDelete(APIView):
    def delete(self, request, task_id: int) -> Response:
        task = get_task_by_id(task_id)
        delete_task(task)
        return Response(status=status.HTTP_204_NO_CONTENT)




       
    

