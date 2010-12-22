# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen.app.layout import master
from zope.app.component.hooks import getSite
from zope.dublincore import interfaces

grok.templatedir("templates")


class MetaTags(grok.Viewlet):
    grok.order(10)
    grok.name('dolmen.metatags')
    grok.context(interfaces.IAttributeAnnotatable)
    grok.viewletmanager(master.Header)

    def update(self):
        self.root = getSite()
        self.DublinCore = interfaces.IZopeDublinCore(self.context, None)

    @property
    def title(self):
        if self.DublinCore is not None and self.context is not self.root:
            return "%s &mdash; %s" % (self.DublinCore.title, self.root.title)
        return self.root.title
