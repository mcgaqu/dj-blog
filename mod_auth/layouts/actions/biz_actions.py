# -*- coding: utf-8 -*-
import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _



def ac_expand_component_layout(modeladmin, request, queryset):
    """
        1. Ejecutar la función definida en cada registro 
    """

    for obj in queryset:
        # import pdb; pdb.set_trace()
        if not obj.locked:
            obj.expand_component_layout()
            message = "Función %s realizada" % obj.alias
            modeladmin.message_user(request, message, level=messages.SUCCESS)
        else:
            message = _("el id:%s, %s no se carga porque está bloqueado") % (obj.id, obj.name)
            modeladmin.message_user(request, message, level=messages.warning)
    return
ac_expand_component_layout.short_description = "Expandir Layout con sus Componentes"


def ac_create_i18n(modeladmin, request, queryset):
    """
        1. Ejecutar la función definida en cada registro 
    """

    for obj in queryset:
        # import pdb; pdb.set_trace()
        if not obj.locked:
            obj.create_i18n()
            message = "Función %s realizada" % obj.alias
        else:
            message = _("el id:%s, %s no se carga porque está bloqueado") % (obj.id, obj.name)
        modeladmin.message_user(request, message, level=messages.SUCCESS)
    return
ac_create_i18n.short_description = "Generar Traducciones"


