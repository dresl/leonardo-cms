from django import forms
from wagtail.core import blocks

from .mixins import CommonBlockMixin


class RichTextBlock(CommonBlockMixin):
    content = blocks.RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        template = 'page/blocks/simple_block.html'
        form_template = 'admin/blocks/simple_block.html'


class MapBlock(CommonBlockMixin):
    marker_title = blocks.CharBlock(max_length=120,
                                    default="Marker Title 'This will be updated after you save changes.'",
                                    classname='half-size-wrapper')
    marker_description = blocks.RichTextBlock()
    zoom_level = blocks.IntegerBlock(
        min_value=0, max_value=18, default='2', required=False)
    location_x = blocks.FloatBlock(default='35.0', required=False)
    location_y = blocks.FloatBlock(default='0.16', required=False)
    marker_x = blocks.FloatBlock(default='51.5', required=False)
    marker_y = blocks.FloatBlock(default='-0.09', required=False)

    @property
    def media(self):
        return forms.Media(
            js=["https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"],
            css={'all': ["https://unpkg.com/leaflet@1.4.0/dist/leaflet.css"]}
        )

    class Meta:
        icon = "fa-globe"
        template = 'page/blocks/map_block.html'
        form_template = 'admin/blocks/map_block.html'
