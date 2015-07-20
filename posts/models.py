from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag


class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    slug = models.TextField(default='')
    body = models.TextField(default='')
    url = models.URLField()
    publish_date = models.DateTimeField()
    # categorias
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title