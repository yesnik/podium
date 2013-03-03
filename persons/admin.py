from django.contrib import admin
from persons.models import *

class PersonAdmin(admin.ModelAdmin):
    fields = ['fio', 'desc', 'phone', 'image']

admin.site.register(Person, PersonAdmin)
admin.site.register(Zhuri)

