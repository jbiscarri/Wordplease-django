from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=250)
    slug = models.TextField(default='')
    body = models.TextField(default='')
    url = models.URLField()
    publish_date = models.DateTimeField()
    # categorias

    def __unicode__(self):
        return self.title