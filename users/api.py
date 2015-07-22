# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer, BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

__author__ = 'joanbiscarri'


# creo user
class UserListAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    # obtengo user
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user.username == user.username:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    # updato user
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user.username == user.username:
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    # elimino user
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user.username == user.username:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class BlogListAPI(APIView):

    def get(self, request, username, order):
        """
        params
        order = asc/desc
        username = name
        """
        orderString = '-username' if order == u'1' else 'username'
        if username != u'':
            users = User.objects.filter(username=username).order_by(orderString)
        else:
            users = User.objects.all().order_by(orderString)
        serializer = BlogSerializer(users, many=True)
        serialized_users = serializer.data  # lista de diccionarios
        return Response(serialized_users)





