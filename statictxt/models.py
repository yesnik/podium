# -*- coding: utf-8 -*-

from django.db import models


class StaticText(models.Model):
    alias = models.SlugField(max_length=40, verbose_name=u'Псевдоним',
                             help_text=u'Системное название статичной области. Латинскими буквами.')
    content = models.TextField(verbose_name=u'Содержание')
    
    def __unicode__(self):
        return self.alias

    class Meta:
        verbose_name = u'Статичный текст'
        verbose_name_plural = u'Статичные тексты'
