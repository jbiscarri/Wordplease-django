# -*- coding: utf-8 -*-
__author__ = 'joanbiscarri'

from rest_framework import serializers
from models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'publish_date' )

