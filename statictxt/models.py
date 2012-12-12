from django.db import models

class StaticText(models.Model):
    alias = models.CharField(max_length=200, verbose_name='Псевдоним')
    content = models.TextField()
    
    def __unicode__(self):
        return self.alias
