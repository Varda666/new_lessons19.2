from django import template

register = template.Library()


@register.filter(name='mediapath')
def path_to_full_path(path_):
    if path_:
        return f'/media/{path_}'
    else:
        return ''


@register.simple_tag(name='mediapath2')
def path_to_full_path(path_):
    if path_:
        return f'/media/{path_}'
    else:
        return ''