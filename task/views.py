from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from user.models import MyUser
from task.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsUser

class TaskView(APIView):
    permission_classes = [IsAuthenticated, IsUser]
    def post(self, request):
        data = request.data
        data['user_data'] = request.user.id
        serialized_data = TaskSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data, status=HTTP_201_CREATED)
        return Response(data=serialized_data.errors)

    def get(self, request):
        tasks = request.user.tasks.all()
        serialized_data = TaskSerializer(tasks, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)
    
    def patch(self, request):
        task_id = request.data.get("id")
        try:
            task = request.user.tasks.get(t_id=task_id)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"},status=HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors)
    def delete(self, request):
        task_id = request.data.get("t_id")
        try:
            task = request.user.tasks.get(t_id=task_id)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"},status=HTTP_404_NOT_FOUND)
        task.delete()
        return Response({"message": "Task deleted successfully"},status=HTTP_204_NO_CONTENT)