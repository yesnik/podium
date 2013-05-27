from django.db import models


class Contest(models.Model):
    """
    Конкурс, проводимый ежегодно
    """
    title = models.CharField(max_length=200, verbose_name='Название конкурса')
    year = models.SlugField(unique=True, max_length=4, verbose_name='Год конкурса')
    description = models.TextField(verbose_name='Описание конкурса')

    def __unicode__(self):
        return unicode(self.year + " " + self.title)
        
    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'
        ordering = ('year', )


class Jury(models.Model):
    """
    Член жюри конкурса
    """
    photo = models.ImageField(upload_to='images/jury', verbose_name='Фото')
    fio = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    position = models.CharField(max_length=150, verbose_name='Должность')
    contest = models.ManyToManyField(Contest)

    def __unicode__(self):
        return self.fio
        
    class Meta:
        verbose_name = 'Жюри'
        verbose_name_plural = 'Жюри'


class Sponsor(models.Model):
    """
    Спонсоры конкурса
    """
    title = models.CharField(max_length=150, verbose_name='Название')
    logo = models.ImageField(upload_to='images/sponsors', verbose_name='Логотип')
    site = models.URLField(verbose_name='Официальный сайт', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    contest = models.ManyToManyField(Contest)

    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Спонсор'
        verbose_name_plural = 'Спонсоры'


class OrganisatorArea(models.Model):
    """
    Зоны ответственности организатора конкурса
    """
    title = models.CharField(max_length=150, verbose_name='Зона ответственности',
        help_text = 'Например, "Техническая группа", "Дирекция"')
    order = models.IntegerField(verbose_name='Порядок следования',
        help_text = 'Зона ответственности с меньшим порядком будет выводиться первее')

    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Зона ответственности организатора'
        verbose_name_plural = 'Зоны ответственности организаторов'


class Organisator(models.Model):
    """
    Организаторы конкурса
    """
    fio = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    photo = models.ImageField(upload_to='images/sponsors', verbose_name='Фото', blank=True)
    position = models.CharField(max_length=150, verbose_name='Должность')
    phone = models.CharField(max_length=150, verbose_name='Телефон', blank=True)
    responsibility_area = models.ForeignKey(OrganisatorArea)

    def __unicode__(self):
        return self.fio
        
    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'


class Winner(models.Model):
    """
    Победитель конкурса - Мисс / Мистер Подиум
    """
    fio = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    vuz = models.ForeignKey('collection.Vuz', blank=True, verbose_name=u'Вуз')
    contest = models.ManyToManyField(Contest, verbose_name=u'Конкурс')
    nomination = models.ForeignKey('collection.Nomination', verbose_name=u'Номинация')
    about = models.TextField(verbose_name='О победителе', blank=True)

    def __unicode__(self):
        return self.fio

    def get_contest_names(self):
        contest_list = self.contest.get_query_set()
        list = []
        if contest_list:
            for contest in contest_list:
                list.append(contest.title)
            return ', '.join(list)

    # В админке поле будет называться не get_nomination, а Номинации
    get_contest_names.short_description = 'Конкурсы'
        
    class Meta:
        verbose_name = 'Мисс / Мистер Подиум'
        verbose_name_plural = 'Мисс / Мистер Подиум'