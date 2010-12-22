# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
import zope.dublincore.interfaces as dc

from z3c.form.field import Fields
from zope.i18nmessageid import MessageFactory
from zeam.form.layout import ComposedForm
from zeam.form.composed import SubForm
from zeam.form.base import SubForm, Actions
from zeam.form.base.datamanager import makeAdaptiveDataManager
from zeam.form.ztk.actions import EditAction

from dolmen.app import security
from dolmen.content import IContent
from dolmen.app.layout import models

_ = MessageFactory("dolmen")


@menu.menuentry(layout.ContextualMenu, order=50)
class Metadata(ComposedForm):
    grok.name('metadatas')
    grok.title(_(u"Metadata"))
    grok.context(IContent)
    grok.require(security.EditContent)

    label = 'Metadata Editing'
    form_name = 'Edit the general dublincore metadata'


class DescriptionMetadata(SubForm):
    grok.view(Metadata)
    grok.context(IContent)
    grok.name('metadata.description')
    grok.order(10)

    label = "Content description"
    form_name = "Content description"
    fields = Fields(dc.IDCDescriptiveProperties)
    dataManager = makeAdaptiveDataManager(dc.IDCDescriptiveProperties)
    actions = Actions(EditAction(u'Update'))
    

class PublishingMetadata(SubForm):
    grok.view(Metadata)
    grok.context(IContent)
    grok.name('metadata.publishing')
    grok.order(20)

    label = "Publishing informations"
    form_name = "Publishing informations"
    fields = Fields(dc.IDCPublishing)
    dataManager = makeAdaptiveDataManager(dc.IDCPublishing)
    actions = Actions(EditAction(u'Update'))


class ExtendedMetadata(SubForm):
    grok.view(Metadata)
    grok.context(IContent)
    grok.name('metadata.extended')
    grok.order(30)

    label = "Extended metadata"
    form_name = "Extended metadata"
    fields = Fields(dc.IDCExtended)
    dataManager = makeAdaptiveDataManager(dc.IDCExtended)
    actions = Actions(EditAction(u'Update'))
