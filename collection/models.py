# -*- coding: utf-8 -*-

from django.db import models
from contest.models import Contest


class Vuz(models.Model):
    """
    Вуз-участник конкурса
    """
    name = models.CharField(max_length=150, verbose_name='Название вуза')
    name_short = models.CharField(max_length=150, verbose_name='Аббревиатура вуза')
    vuz_url = models.SlugField(verbose_name='Ярлык для использования в url')

    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'ВУЗ'
        verbose_name_plural = 'ВУЗы'


class Author(models.Model):
    """
    Автор коллекции
    """
    fio = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    about = models.TextField(verbose_name='Об авторе')
    birthday = models.DateField(verbose_name='Дата рождения')
    vuz = models.ForeignKey(Vuz, verbose_name='ВУЗ')

    def __unicode__(self):
        return self.fio

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Nomination(models.Model):
    """
    Номинация, по которой проводится конкурс
    """
    title = models.CharField(max_length=150, verbose_name = 'Название номинации')
    nomination_url = models.SlugField(verbose_name='Ярлык для использования в url', 
        help_text='Например, one_model или teatr_mod')
    description = models.TextField(verbose_name='Описание номинации', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Номинация'
        verbose_name_plural = 'Номинации'


class Collection(models.Model):
    """
    Коллекция, принимающая участие в конкурсе
    """
    title = models.CharField(max_length=100, verbose_name=u'Название')
    author = models.ManyToManyField(Author, verbose_name=u"Автор")
    nomination = models.ManyToManyField(Nomination, verbose_name=u'Номинация')
    contest = models.ManyToManyField(Contest, verbose_name=u'Конкурс(ы)')
    description = models.TextField(verbose_name=u'Описание коллекции')

    @staticmethod
    def get_vuz_collections_by_year(vuz_url, year):
        return Collection.objects.filter(contest__year=year, author__vuz__vuz_url=vuz_url)

    def __unicode__(self):
        return self.title

    def get_nominations(self):
        nomination_list = self.nomination.get_query_set()
        nominations_str = ''
        for nomination in nomination_list:
            nominations_str += ', ' + nomination.title
        return nominations_str.lstrip(', ')
    # В админке поле будет называться не get_nomination, а Номинации
    get_nominations.short_description = 'Номинации'

    def get_contest_years(self):
        contest_list = self.contest.get_query_set()
        contests_str = ''
        for contest in contest_list:
            contests_str += ', ' + str(contest.year)
        return contests_str.lstrip(', ')
    # В админке поле будет называться не get_nomination, а Номинации
    get_contest_years.short_description = 'Год конкурса'
        
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


PLACE_CHOICES = (
    (1, u'1 место'),
    (2, u'2 место'),
    (3, u'3 место'),
)
        
class Prizer(models.Model):
    """
    Коллекция, победивщая в конкурсе в какой-то номинации
    """
    contest = models.ForeignKey(Contest, verbose_name=u'Конкурс')
    nomination = models.ForeignKey(Nomination, verbose_name=u'Номинация')
    place = models.IntegerField(choices=PLACE_CHOICES, verbose_name=u'Место')
    collection = models.ForeignKey(Collection, verbose_name=u'Коллекция')
    
    def __unicode__(self):
        return self.collection.title
        
    class Meta:
        verbose_name = 'Призер'
        verbose_name_plural = 'Призеры'
