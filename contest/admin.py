from django.contrib import admin
from contest.models import Contest, Jury


class JuryAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position',)
    filter_horizontal = ('contest',)


class ContestAdmin(admin.ModelAdmin):
    list_display = ('year', 'title',)
    order = '-year'


admin.site.register(Contest, ContestAdmin)
admin.site.register(Jury, JuryAdmin)