from django.db import models
from blog.models import Page

from mysite.settings import UPLOADS_DIR
from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location=UPLOADS_DIR)

class Person(models.Model):
    fio = models.CharField(max_length=200, verbose_name='Ф.И.О.', blank=True)
    desc = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='static/uploads')
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.fio