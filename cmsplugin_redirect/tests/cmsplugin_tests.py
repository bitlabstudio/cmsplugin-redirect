"""Tests for models of the ``cmsplugin_redirect``` application."""
from django.test import TestCase

from mock import Mock

from ..cms_plugins import ForceResponse, ForceRedirectPlugin
from .factories import ForceRedirectPluginModelFactory, TitleFactory


class CMSInterestGroupPluginTestCase(TestCase):
    """Tests for the ``CMSInterestGroupPlugin`` cmsplugin."""
    longMessage = True

    def setUp(self):
        self.plugin = ForceRedirectPluginModelFactory(
            page_link=TitleFactory().page)
        self.no_link_plugin = ForceRedirectPluginModelFactory(page_link=None)
        self.cmsplugin = ForceRedirectPlugin()
        self.page = TitleFactory(slug='home').page
        self.request = Mock(current_page=self.page)

    def test_render(self):
        # should redirect to the page
        self.assertRaises(
            ForceResponse,
            self.cmsplugin.render,
            context={'request': self.request},
            instance=self.plugin,
            placeholder=None)
        # should raise exception because no child exists
        self.assertRaises(
            Exception,
            self.cmsplugin.render,
            context={'request': self.request},
            instance=self.no_link_plugin,
            placeholder=None)
