from django.core.context_processors import request


def menu(request):
    return {"var": "It is my var 1 from template context processor!"}


def nik(request):
    return {'nik': 'This is Nik var from context processor'}