from django.db import models



class Tag(models.Model):
    title = models.CharField(max_length=250)

    def __unicode__(self):
        return self.title