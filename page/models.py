# -*- coding: utf-8 -*-

from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    page_url = models.SlugField(help_text='URL, по которому будет доступна страница', verbose_name='URL страницы')
    content = models.TextField(verbose_name='Содержимое страницы')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'