"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from posts.api import PostListAPI, PostDetailAPI, PostSetAPI
from users.api import UserDetailAPI, UserListAPI, BlogListAPI
from users.views import LoginView, SignupView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'posts.views.listAll', name='blogs_all'),
    url(r'^blogs/$', 'posts.views.list', name='blogs_list'),
    url(r'^blogs/(?P<username>[-\w]+)$', 'posts.views.blog', name='blog_detail'),
    url(r'^blogs/(?P<username>[-\w]+)/(?P<pk>[0-9]+)', 'posts.views.post', name='post_detail'),
    url(r'^new-post/$', 'posts.views.create', name='new_post'),

    # User URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', 'users.views.logout', name='users_logout'),
    url(r'^signup', SignupView.as_view(), name='users_signup'),

    # Api URLs
    url(r'^api/1.0/users$', UserListAPI.as_view(), name='users_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),
    url(r'^api/1.0/blogs/(?P<username>[a-zA-Z]*)(/*)(?P<order>[0-9]*)$', BlogListAPI.as_view(), name='blogs_list_api'),
    url(r'^api/1.0/post/$', PostSetAPI.as_view(), name='post_list_api'),
    url(r'^api/1.0/post/(?P<pk>[0-9]+)$', PostDetailAPI.as_view(), name='post_list_api'),
    url(r'^api/1.0/posts/(?P<username>[-\w]*)(/*)((?P<search>search=[-\w]*)*)(/*)((?P<order>order=[-\w]*)*)$', PostListAPI.as_view(), name='post_list_api'),




]
