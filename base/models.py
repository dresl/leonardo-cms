from django.db import models

from modelcluster.fields import ParentalKey
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, ImageSliderBlock

from wagtailmenus.models import MenuPage
from wagtailmenus.panels import menupage_panel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    FieldRowPanel,
    TabbedInterface,
    ObjectList
)
from wagtail.core import blocks
from wagtail.search import index
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.fields import ImageField

from .blocks import RichTextBlock, MapBlock


class StandardPage(Page):

    template = 'page/standard_page.html'

    # fields

    body = StreamField([
        ('text', RichTextBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
        ('image_slider', ImageSliderBlock()),
    ], blank=True)

    sidebar = StreamField([
        ('text', RichTextBlock())
    ], blank=True)

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='pages'
    )

    full_width = models.BooleanField(default=False, help_text='Fullscreen page layout')

    display_page_title = models.BooleanField(default=True, help_text='Display title on page detail')

    # panels

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    promote_panels = Page.promote_panels + []

    settings_panels = [
        MultiFieldPanel([
            ImageChooserPanel('featured_image'),
            FieldPanel('full_width'),
            FieldPanel('display_page_title')
        ], heading='Common')
    ] + Page.settings_panels

    sidebar_content_panels = [
        StreamFieldPanel('sidebar')
    ]

    # search fields

    search_fields = Page.search_fields + [
        index.SearchField('search_description', partial_match=True),
        index.SearchField('body', partial_match=True)
    ]

    # tabs

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(sidebar_content_panels, heading='Sidebar'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(settings_panels, heading='Settings', classname="settings"),
    ])
