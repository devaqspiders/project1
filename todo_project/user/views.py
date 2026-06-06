from django.shortcuts import render
from rest_framework.views import APIView
from user.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
class UserView(APIView):
    def post(self,request):
        user_data = request.data
        serialized_data = UserSerializer(data=user_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data={'message':'user created successfully'}, status=HTTP_201_CREATED)
        return Response(data=serialized_data.errors)