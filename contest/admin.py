# -*- coding: utf-8 -*-

from django.contrib import admin
from contest.models import (Contest, Jury, Sponsor, 
    Organisator, OrganisatorArea, Winner)

# Импортируем настройки приложения django-attachments
from attachments.admin import AttachmentInlines


class JuryAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position',)
    filter_horizontal = ('contest',)


class ContestAdmin(admin.ModelAdmin):
    list_display = ('year', 'title',)
    order = '-year'


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('title', 'site',)
    filter_horizontal = ('contest',)


class OrganisatorAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position',)


class OrganisatorAreaAdmin(admin.ModelAdmin):
    list_display = ('title', 'order',)


class WinnerAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
    list_display = ('fio', 'get_contest_names', 'nomination', 'vuz',)
    filter_horizontal = ('contest',)


admin.site.register(Contest, ContestAdmin)
admin.site.register(Jury, JuryAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Organisator, OrganisatorAdmin)
admin.site.register(OrganisatorArea, OrganisatorAreaAdmin)
admin.site.register(Winner, WinnerAdmin)