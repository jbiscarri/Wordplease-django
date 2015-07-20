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
from users.views import LoginView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'posts.views.listAll', name='blogs_all'),
    url(r'^blogs/$', 'posts.views.list', name='blogs_list'),
    url(r'^blogs/(?P<username>[a-zA-Z]+)$', 'posts.views.blog', name='blog_detail'),
    url(r'^blogs/(?P<username>[a-zA-Z]+)/(?P<pk>[0-9]+)', 'posts.views.post', name='post_detail'),
    url(r'^new-post/$', 'posts.views.create', name='new_post'),

    # User URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', 'users.views.logout', name='users_logout'),


]
