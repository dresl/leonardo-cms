from wagtail.images.formats import Format, register_image_format, unregister_image_format

# unregister default image formats in richtext component
unregister_image_format('fullwidth')
unregister_image_format('left')
unregister_image_format('right')


register_image_format(Format('full_width', 'Full width',
                             'richtext-image full-width', 'scale-100'))

register_image_format(Format('left', 'Left',
                             'richtext-image float-left', 'max-500x300'))

register_image_format(Format('right', 'Right',
                             'richtext-image float-right', 'max-500x300'))

register_image_format(Format('center', 'Center',
                             'richtext-image mx-auto d-block', 'max-500x300'))
