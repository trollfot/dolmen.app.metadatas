# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen.app.layout import master
from zope.i18nmessageid import MessageFactory
from zope.app.component.hooks import getSite
from zope.dublincore.interfaces import IZopeDublinCore
from zope.annotation.interfaces import IAttributeAnnotatable

grok.templatedir("templates")
_ = MessageFactory("dolmen")


class ContentInformations(grok.Viewlet):
    grok.name('metadata.contentinformation')
    grok.context(IAttributeAnnotatable)
    grok.viewletmanager(master.DolmenBelowBody)
    grok.order(20)

    creation = u""
    modification = u""
    
    def update(self):
        dc = IZopeDublinCore(self.context)
        formatter = self.request.locale.dates.getFormatter('dateTime')

        if dc.created:
            self.creation = _(
                u"Created by ${name} the ${date}",
                mapping={'name': dc.creators and dc.creators[0],
                         'date': formatter.format(dc.created)}
                )
        
        if dc.modified:
            self.modification =  _(
                u"Last modified the ${date}",
                mapping={'date': formatter.format(dc.modified)}
                )
