from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from user.models import MyUser
from task.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
class TaskView(APIView):
    def post(self, request):
        data = request.data
        data['user_data'] = request.user
        serialized_data = TaskSerializer(data=data)
        if serialized_data.is_valid():
            return Response(data=serialized_data.data, status=HTTP_201_CREATED)

    def get(self, request):
        tasks = Task.objects.all()
        

        