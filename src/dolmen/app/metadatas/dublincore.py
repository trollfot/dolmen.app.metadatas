# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
import zope.dublincore.interfaces as dc

from z3c.form.field import Fields
from zope.i18nmessageid import MessageFactory
from megrok.z3cform.composed import ComposedForm

import dolmen.forms.crud as crud
from dolmen.content import IContent
from dolmen.app.layout import models, ContextualMenuEntry

_ = MessageFactory("dolmen")


class Metadata(ComposedForm, ContextualMenuEntry):
    grok.name('metadatas')
    grok.title(_(u"Metadata"))
    grok.context(IContent)
    grok.require('dolmen.content.Edit')

    label = 'Metadata Editing'
    form_name = 'Edit the general dublincore metadata'


class DescriptionMetadata(models.SubForm, crud.Edit):
    grok.view(Metadata)
    grok.context(IContent)
    grok.name('metadata.description')
    grok.order(10)

    label = "Content description"
    form_name = "Content description"
    fields = Fields(dc.IDCDescriptiveProperties)
    

class PublishingMetadata(models.SubForm, crud.Edit):
    grok.view(Metadata)
    grok.context(IContent)
    grok.name('metadata.publishing')
    grok.order(20)

    label = "Publishing informations"
    form_name = "Publishing informations"
    fields = Fields(dc.IDCPublishing)


class ExtendedMetadata(models.SubForm, crud.Edit):
    grok.view(Metadata)
    grok.context(IContent)
    grok.name('metadata.extended')
    grok.order(30)

    label = "Extended metadata"
    form_name = "Extended metadata"
    fields = Fields(dc.IDCExtended)
