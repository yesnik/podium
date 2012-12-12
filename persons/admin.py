from django.contrib import admin
from persons.models import *

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Личности', {'fields': ['fio', 'desc', 'image'], 'classes': ['collapse']}),
    ]

admin.site.register(Person, PersonAdmin)