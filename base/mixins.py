from django import forms
from django.forms.widgets import NumberInput

from wagtail_blocks.blocks import ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.core.blocks import RichTextBlock as WRichTextBlock, CharBlock, FieldBlock


class IntegerRangeBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.IntegerField(widget=NumberInput(attrs={
            'type':'range',
            'step': '1',
            'max': '12',
            'min': '1',
            'class': 'leo-wagtail-range-input'
        }))
        super().__init__(**kwargs)


class DimensionBlockMixin(blocks.StructBlock):
    small_width = IntegerRangeBlock()
    large_width = IntegerRangeBlock()
