from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user = user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return  Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)