from django.http import HttpResponseRedirect
from django.templatetags.static import static
from django.utils.html import format_html

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler, BlockElementHandler
from wagtail.core import hooks


def register_text_align_feature(align):
    feature_name = f'text-{align}'
    type_ = align.upper()
    control = {
        'type': type_,
        'label': align,
        'description': f'{align.capitalize()} text',
        'style': {
            'textAlign': align,
            'display': 'block'
        }
    }
    db_format = {
        'from_database_format': {f'p[class="text-{align}"]': InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: f'p class="text-{align}"'}},
    }
    return (feature_name, type_, control, db_format)


# global admin hooks

@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add main.css to the admin."""
    css_links = """
        <link rel="stylesheet" href="{main}">
        <link rel="stylesheet" href="{fontawesome}">
    """.format(main=static("css/admin/main.css"), fontawesome=static("wagtailfontawesome/css/fontawesome.css"))
    return format_html(css_links)


@hooks.register('after_edit_page')
def do_after_page_edit(request, page):
    return HttpResponseRedirect(request.path)


# draftail hooks

@hooks.register('register_rich_text_features')
def make_h1_default(features):
    features.default_features.append('h1')


@hooks.register('register_rich_text_features')
def register_center_feature(features):
    """
    Registering the `text-center` feature.
    """
    f_name, type_, control, db_format = register_text_align_feature('center')
    features.register_editor_plugin('draftail', f_name,
                                    draftail_features.InlineStyleFeature(control))
    features.register_converter_rule(
        'contentstate', f_name, db_format)
    features.default_features.append('text-center')


@hooks.register('register_rich_text_features')
def register_right_feature(features):
    """
    Registering the `text-right` feature.
    """
    f_name, type_, control, db_format = register_text_align_feature('right')
    features.register_editor_plugin('draftail', f_name,
                                    draftail_features.InlineStyleFeature(control))
    features.register_converter_rule(
        'contentstate', f_name, db_format)
    features.default_features.append('text-right')


@hooks.register('register_rich_text_features')
def register_justify_feature(features):
    """
    Registering the `text-justify` feature.
    """
    f_name, type_, control, db_format = register_text_align_feature('justify')
    features.register_editor_plugin('draftail', f_name,
                                    draftail_features.InlineStyleFeature(control))
    features.register_converter_rule(
        'contentstate', f_name, db_format)
    features.default_features.append('text-justify')
