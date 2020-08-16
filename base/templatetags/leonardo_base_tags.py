from django import template

from base.mixins import CommonBlockMixin

register = template.Library()


# common filters

@register.filter
def get_fields(obj):
    """Get python object attributes"""
    print(obj.__dict__)
    return ''


@register.filter
def snake_case(text):
    """Coverts string to snake case. E.g. `Dummy-Text 1` wiil be `dummy_text_1`"""
    return text.replace('-', '_').replace('.', '_').replace(' ', '_').lower()


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
        if field.block.name not in common_blocks:
            res.append(field)
    return res
