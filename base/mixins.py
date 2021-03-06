from django import forms
from django.forms.widgets import NumberInput
from wagtail.core import blocks


class IntegerRangeBlock(blocks.FieldBlock):
    def __init__(self, max_value='12', min_value='1', default_value='12', **kwargs):
        self.field = forms.IntegerField(widget=NumberInput(attrs={
            'type': 'range',
            'step': '1',
            'max': max_value,
            'min': min_value,
            'value': default_value
        }))
        super().__init__(**kwargs)


class CommonBlockMixin(blocks.StructBlock):
    small_width = IntegerRangeBlock()
    small_offset = IntegerRangeBlock(
        max_value='11', min_value='0', default_value='0')
    large_width = IntegerRangeBlock()
    large_offset = IntegerRangeBlock(
        max_value='11', min_value='0', default_value='0')
    remove_padding = blocks.BooleanBlock(required=False)
