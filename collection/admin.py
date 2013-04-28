from django.contrib import admin
from collection.models import Collection, Author, Vuz, Nomination


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fio', 'birthday', 'vuz')
    search_fields = ('fio','vuz__name',)
    ordering = ('-fio',)


class CollectionAdmin(admin.ModelAdmin):
    filter_horizontal = ('author', 'nomination', 'contest',)
    ordering = ('-contest__year',)


class NominationAdmin(admin.ModelAdmin):
    list_display = ('title', 'nomination_url',)


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Author, AuthorAdmin) 
admin.site.register(Vuz) 
admin.site.register(Nomination, NominationAdmin) 