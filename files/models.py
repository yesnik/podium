from django.db import models
from blog.models import Page

class File(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True)
    file = models.FileField(upload_to="static/uploads/files")
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.title