from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from user.models import MyUser
from task.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
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