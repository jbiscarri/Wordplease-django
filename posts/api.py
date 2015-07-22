# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q



__author__ = 'joanbiscarri'


class PostListAPI(APIView):

    # si es autenticado y estoy viendo sus posts, se muestran los no publicados tb, si no, solo los publicados
    def get(self, request, username, search, order):
        users = User.objects.filter(username=username)
        if len(users) > 0:
            if search is None:
                search = u''
            search = search.replace('search=', '')

            if order is None:
                posts = Post.objects.filter((Q(body__contains=search) | Q(title__contains=search)) & Q(owner=users[0])).order_by('-publish_date')
            elif order == 'title' or order == '-title' or order == 'publish_date' or order == '-publish_date':
                order = order.replace('order=', '')
                posts = Post.objects.filter((Q(body__contains=search) | Q(title__contains=search)) & Q(owner=users[0])).order_by(order)
            else:
                return Response('Order parameter incorrect, have to be: title, -title, publish_date, -publish_date', status=status.HTTP_400_BAD_REQUEST)
            # muestro todos los posts (incluso no publicados) si son mios o soy superadmin
            if not request.user.is_superuser and request.user.username != username:
                posts = posts.filter(published=True)
            serializer = PostListSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PostSetAPI(APIView):

    def post(self, request):
        if request.user is not None and request.user.is_active:
            request.data[u'owner'] = request.user.pk
            request.data[u'published'] = True
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                new_post = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class PostDetailAPI(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.published or request.user.is_superuser or request.user.username == post.owner.username:
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_superuser or request.user.username == post.owner.username:
            serializer = PostSerializer(instance=post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_superuser or request.user.username == post.owner.username:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

