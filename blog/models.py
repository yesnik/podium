﻿from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
    
    def __unicode__(self):
        return self.title