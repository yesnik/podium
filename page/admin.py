# -*- coding: utf-8 -*-

from django.contrib import admin
from page.models import Page

# Импортируем настройки приложения django-attachments
from attachments.admin import AttachmentInlines

class PageAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
    list_display = ('title', )

admin.site.register(Page, PageAdmin)