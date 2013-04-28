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
    nomination_url = models.SlugField(verbose_name='Ярлык для использования в url')
    description = models.TextField(verbose_name='Описание номинации')

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
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

        

