# -*- coding: utf-8 -*-
from posts.models import Post

__author__ = 'joanbiscarri'

from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner']
