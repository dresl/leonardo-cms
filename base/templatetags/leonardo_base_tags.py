from django import template

register = template.Library()
from base.mixins import CommonBlockMixin


@register.filter
def get_fields(obj):
    print(obj.__dict__)
    return ''

@register.filter
def snake_case(text):
    return text.replace('-', '_').replace('.', '_')


# admin blocks filters

@register.filter
def get_common_fields(fields):
    """Returns dimensions and other block common fields (CommonBlockMixin)"""
    res = []
    common_blocks = [block for block in CommonBlockMixin.declared_blocks]
    for field in fields:
        if field.block.name in common_blocks:
            res.append(field)
    return res

@register.filter
def get_extra_fields(fields):
    """Return fields from block except fields from CommonBlockMixin"""
    res = []
    common_blocks = [block for block in CommonBlockMixin.declared_blocks]
    for field in fields:
        if not field.block.name in common_blocks:
            res.append(field)
    return res
