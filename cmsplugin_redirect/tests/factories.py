"""Factories for the models of the ``cmsplugin_redirect`` app."""
from django.utils.timezone import now

import factory
from cms.models import Page, Site
from django_libs.tests.factories import UserFactory

from ..models import ForceRedirectPluginModel


class SiteFactory(factory.Factory):
    FACTORY_FOR = Site


class PageFactory(factory.Factory):
    FACTORY_FOR = Page

    site = factory.SubFactory(SiteFactory)
    published = True
    template = 'standard.html'
    created_by = factory.SubFactory(UserFactory)
    changed_by = factory.SubFactory(UserFactory)
    rght = 5
    lft = 4
    in_navigation = True
    tree_id = 1
    publisher_state = 1
    publication_date = factory.LazyAttribute(lambda a: now())
    level = 1
    publisher_is_draft = True


class ForceRedirectPluginModelFactory(factory.Factory):
    """Factory for the ``ForceRedirectPluginModel`` model."""
    FACTORY_FOR = ForceRedirectPluginModel

    page_link = factory.SubFactory(PageFactory)
