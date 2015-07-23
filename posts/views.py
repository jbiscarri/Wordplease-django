from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required

def listAll(request):
    posts = Post.objects.filter(published=True).order_by('-publish_date')
    context = {
        # 'post_list': posts[:10],
        'post_list': posts,
        'username': None
    }
    return render(request, 'posts/posts.html', context)

def list(request):
    users = User.objects.all().order_by('username')
    context = {'user_list': users}
    return render(request, 'posts/blogs.html', context)

def blog(request, username):
    possible_user = User.objects.filter(username=username)
    #now = datetime.now()
    user = possible_user[0] if len(possible_user) >= 1 else None
    if user is not None:
        posts = Post.objects.filter(owner=user, published=True).order_by('-publish_date').select_related('owner')
        context = {
            'post_list': posts,
            'username': user.username
        }
        return render(request, 'posts/posts.html', context)
    else:
        return HttpResponseNotFound()

def post(request, username, pk):
    possible_post = Post.objects.filter(pk=pk)
    post = possible_post[0] if len(possible_post) >= 1 else None
    if post is not None:
       context = {
            'post': post
       }
       return render(request, 'posts/post_detail.html', context)
    else:
        return HttpResponseNotFound()

@login_required()
def create(request):
    success_message = ''
    if request.method == 'GET':
        form = PostForm()
    else:
        post_with_owner = Post()
        post_with_owner.owner = request.user
        form = PostForm(request.POST, instance=post_with_owner)
        if form.is_valid():
            new_post = form.save()
            form = PostForm()
            success_message = 'Guardado con Correctamente! '
            success_message += '<a href="{0}">'.format(reverse('post_detail', args=[new_post.owner.username, new_post.pk]))
            success_message += 'Ver Post creado'
            success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'posts/new_post.html', context)