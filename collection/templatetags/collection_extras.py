from django import template
from collection.models import Author, Collection

register = template.Library()

def cut(value, arg):
    "Removes all values of arg from the given string"
    return value.replace(arg, '')


def addprefix(value, arg):
    "Adds Mister or whatever you choosen"
    return arg + ' ' + value

register.filter('addprefix', addprefix)


@register.filter
def get_about(value):

    id_collection = value.id
    authors = Author.objects.filter(collection__id=id_collection)
    about_list = []
    for author in authors:
        about_list.append(author.about)
    return ', '.join(about_list)


@register.filter
def getCollectionSum(value):
    sum = Collection.objects.filter(author__vuz__id = value)
    return len(sum)

  
    
