from django.http import HttpResponseRedirect
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.core import hooks


# global admin hooks

@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add main.css to the admin."""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/admin/main.css")
    )


@hooks.register('after_edit_page')
def do_after_page_edit(request, page):
    return HttpResponseRedirect(request.path)


# draftail hooks
