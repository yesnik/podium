from django.db import models

class StaticText(models.Model):
    alias = models.CharField(max_length=200, verbose_name='Псевдоним')
    content = models.TextField(verbose_name='Содержание')
    
    class Meta:
        verbose_name = 'Статичный текст'
        verbose_name_plural = 'Статичные тексты'
    
    def __unicode__(self):
        return self.alias
