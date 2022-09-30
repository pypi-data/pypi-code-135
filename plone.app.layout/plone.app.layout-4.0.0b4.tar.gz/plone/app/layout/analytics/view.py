from plone.registry.interfaces import IRegistry
from plone.base.interfaces import ISiteSchema
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.interface import implementer
from zope.viewlet.interfaces import IViewlet


@implementer(IViewlet)
class AnalyticsViewlet(BrowserView):

    render = ViewPageTemplateFile("view.pt")

    def __init__(self, context, request, view, manager):
        super().__init__(context, request)
        self.__parent__ = view
        self.view = view
        self.manager = manager

    @property
    def webstats_js(self):
        registry = getUtility(IRegistry)
        site_settings = registry.forInterface(ISiteSchema, prefix="plone", check=False)
        try:
            return site_settings.webstats_js or ""
        except AttributeError:
            return ""

    def update(self):
        """The viewlet manager _updateViewlets requires this method"""
        pass
