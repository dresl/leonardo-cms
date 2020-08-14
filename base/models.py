from django.db import models

from modelcluster.fields import ParentalKey
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

from wagtailmenus.models import MenuPage
from wagtailmenus.panels import menupage_panel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    FieldRowPanel
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel


class StandardPage(Page):
    body = StreamField([
        ('header', HeaderBlock()),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
        ('image_slider', ImageSliderBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
