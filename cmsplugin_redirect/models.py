"""Models for the ``cmsplugin_redirect`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page


class ForceRedirectPluginModel(CMSPlugin):
    """
    Plugin model to specify a custom redirect action as placeholder.

    :page_link: Defines which child the plugin redirects to.

    """
    page_link = models.ForeignKey(
        Page,
        verbose_name=_('Child'),
        blank=True, null=True,
    )
