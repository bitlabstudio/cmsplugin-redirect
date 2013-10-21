"""CMS Plugins for the ``cmsplugin_redirect`` app."""
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect

from cms.plugins.link.forms import LinkForm
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import ForceRedirectPluginModel
from .middleware import ForceResponse


class ForceRedirectPlugin(CMSPluginBase):
    model = ForceRedirectPluginModel
    form = LinkForm
    name = _('Redirect action')
    admin_preview = False

    def render(self, context, instance, placeholder):
        current_page = context['request'].current_page
        # if the user defined a page and that isn't the current one, redirect
        # there
        if instance.page_link and instance.page != instance.page_link:
            url = instance.page_link.get_absolute_url()
        else:
            # otherwise try to redirect to the first child if present
            try:
                url = '/{}/'.format(
                    current_page.get_children()[0].get_path())
            except IndexError:
                raise Exception('No child page found!')

        raise ForceResponse(HttpResponseRedirect(url))


plugin_pool.register_plugin(ForceRedirectPlugin)
