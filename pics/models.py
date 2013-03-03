from django.db import models
from blog.models import Page

class Pic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=True)
    image = models.ImageField(upload_to="static/uploads")
    page = models.ForeignKey(Page)
    
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
    
    def __unicode__(self):
        return self.title