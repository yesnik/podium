from django.db import models
from blog.models import Page

class Pic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True)
    image = models.ImageField(upload_to="static/uploads")
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.title