from django import template

register = template.Library()


@register.filter
def get_fields(obj):
    print(obj.__dict__)
    return ''


@register.filter
def snake_case(text):
    return text.replace('-', '_').replace('.', '_')
