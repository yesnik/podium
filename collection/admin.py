# -*- coding:utf-8 -*-

from django.contrib import admin
from collection.models import Collection, Author, Vuz, Nomination, Prizer

# Импортируем настройки приложения django-attachments
from attachments.admin import AttachmentInlines


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fio', 'birthday', 'vuz')
    search_fields = ('fio','vuz__name',)
    ordering = ('-fio',)


class CollectionAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
    filter_horizontal = ('author', 'nomination', 'contest',)
    list_display = ('title', 'get_nominations', 'get_contest_years',)
    ordering = ('-contest__year',)

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )


class NominationAdmin(admin.ModelAdmin):
    list_display = ('title', 'nomination_url',)


class PrizerAdmin(admin.ModelAdmin):
    list_display = ('collection', 'nomination', 'place', 'contest')
    ordering = ('-contest__year', 'nomination__title', 'place',)


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Author, AuthorAdmin) 
admin.site.register(Vuz) 
admin.site.register(Nomination, NominationAdmin)
admin.site.register(Prizer, PrizerAdmin) 