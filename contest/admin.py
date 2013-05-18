from django.contrib import admin
from contest.models import Contest, Jury, Sponsor


class JuryAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position',)
    filter_horizontal = ('contest',)


class ContestAdmin(admin.ModelAdmin):
    list_display = ('year', 'title',)
    order = '-year'


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('title', 'site',)
    filter_horizontal = ('contest',)


admin.site.register(Contest, ContestAdmin)
admin.site.register(Jury, JuryAdmin)
admin.site.register(Sponsor, SponsorAdmin)