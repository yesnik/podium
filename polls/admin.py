from django.contrib import admin
from polls.models import Poll, Choice

#Делаем так, чтобы Choice отображалось в модели Poll
#class ChoiceInline(admin.StackedInline):  #StackedInline - отображаются строками
class ChoiceInline(admin.TabularInline):
    model = Choice
    #количество отображаемых эл-тов
    extra = 3
    
class ChoiceAdmin(admin.ModelAdmin):
    #Филдсеты
    fieldsets = [
        ('Опрос',  {'fields': ['poll']}),
        ('Ответы', {'fields': ['choice', 'votes'], 
                    #Филдсет свернут - collapse
                    'classes': ['collapse']
                    }
        ),
    ]
    

class PollAdmin(admin.ModelAdmin):
    #порядок следования полей
    fields = ['pub_date', 'question']
    #Вставляет в модель Poll др. модель согласно настройкам ChoiceInline
    inlines = [ChoiceInline]
    #Установка колонок, которые отображаются на главной странице модели
    list_display = ('question', 'pub_date', 'was_published_recently')
    #Фильтр по указанным полям
    list_filter = ['pub_date']
    #Поиск по указанным полям
    search_fields = ['question']
    #Иерархия по датам
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)