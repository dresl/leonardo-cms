from django import forms
from django.forms.widgets import NumberInput

from wagtail_blocks.blocks import ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from .mixins import DimensionBlockMixin


class RichTextBlock(DimensionBlockMixin):
    text = blocks.RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        template = 'wagtail_blocks/rich_text.html'
        form_template = 'admin_blocks/rich_text.html'
