from django.contrib import admin
from blog.models import Page
from pics.models import Pic
from files.models import File
from persons.models import Person


class ChoiceInline(admin.StackedInline):
    model = Pic
    #количество отображаемых эл-тов
    extra = 2
    
class FileInline(admin.StackedInline):
    model = File
    #количество отображаемых эл-тов
    extra = 2
    
class PersonInline(admin.StackedInline):
    model = Person
    #количество отображаемых эл-тов
    extra = 2
    fieldsets = [
        ('Подробнее', {'fields': ['fio', 'desc', 'image'], 'classes': ['collapse']}),
    ]

class PicAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, FileInline, PersonInline]
    

admin.site.register(Page, PicAdmin)