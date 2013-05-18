from django.db import models


class Contest(models.Model):
    """
    Конкурс, проводимый ежегодно
    """
    title = models.CharField(max_length=200, verbose_name='Название конкурса')
    year = models.SlugField(unique=True, max_length=4, verbose_name='Год конкурса')
    description = models.TextField(verbose_name='Описание конкурса')

    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'


class Jury(models.Model):
    """
    Член жюри конкурса
    """
    photo = models.ImageField(upload_to='images/jury')
    fio = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    position = models.CharField(max_length=150, verbose_name='Должность')
    contest = models.ManyToManyField(Contest)

    def __unicode__(self):
        return self.fio
        
    class Meta:
        verbose_name = 'Жюри'
        verbose_name_plural = 'Жюри'