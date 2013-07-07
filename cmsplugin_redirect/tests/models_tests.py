"""Tests for the models of the ``cmsplugin_redirect`` app."""
from django.test import TestCase

from .factories import ForceRedirectPluginModelFactory


class ForceRedirectPluginModelTestCase(TestCase):
    """Tests for the ``ForceRedirectPluginModel`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``ForceRedirectPluginModel`` model."""
        forceredirectpluginmodel = ForceRedirectPluginModelFactory()
        self.assertTrue(forceredirectpluginmodel.pk)
