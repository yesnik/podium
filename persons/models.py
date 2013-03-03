from django.db import models
from blog.models import Page

from mysite.settings import UPLOADS_DIR
from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location=UPLOADS_DIR)

class Person(models.Model):
    fio = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    desc = models.TextField(verbose_name='Описание')
    phone = models.CharField(max_length=60, verbose_name='Контактный телефон', blank=True)
    image = models.ImageField(upload_to='static/uploads', verbose_name='Фото', blank=True)
    
    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'
    
    def __unicode__(self):
        return self.fio
        
class Zhuri(models.Model):
    fio = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    desc = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='static/uploads', blank=True)
    year = models.CharField(max_length=200, verbose_name='Год конкурса')
    
    class Meta:
        verbose_name = 'Член жюри'
        verbose_name_plural = 'Члены жюри'
        ordering = ['-year']
    
    def __unicode__(self):
        return self.fio