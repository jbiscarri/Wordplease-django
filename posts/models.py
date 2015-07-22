from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag


class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    slug = models.TextField(default='', blank=True, null=True)
    body = models.TextField(default='')
    url = models.URLField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField()
    # categorias
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return self.title