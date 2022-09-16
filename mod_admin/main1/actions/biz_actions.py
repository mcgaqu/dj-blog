# -*- coding: utf-8 -*-
from http.client import responses
import os, sys
from pickle import NONE
from importlib import import_module

from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _

from mod_admin.utils.base import get_biz, get_company

#-----------------------------------

def display_function_name(**kwargs):
    data = kwargs['function_name']
    response = {
        'message': data,
        'level': messages.SUCCESS,
        'data': data
    }
    return response
display_function_name.short_description = "Display function name"
display_function_name.kwargs = ''
display_function_name.response = 'data'

#------------------------------------

def call_execute_job(modeladmin, request, queryset, job_function=None):
    """
        Salvar los registros seleccionados
    """
    kwargs = {
        'target': modeladmin,
        'request': request,
        'queryset': queryset,
        #-----------------
        # 'biz': get_biz(),
        # 'company': get_company()
    }
    response = job_function(**kwargs)
    modeladmin.message_user(request, response['message'], response['level'])
    return response['data']
call_execute_job.short_description = "Execute Job Function"   


#---------------------------------

def get_time_now(**kwargs):
    data = timezone.now()
    response = {
        'message': 'Es la hora %s' % data,
        'level': messages.SUCCESS,
        'data': data
    }
    return response
get_time_now.short_description = "Obtener la hora"
get_time_now.kwargs = ''
get_time_now.response = 'data'


def ac_get_time_now(modeladmin, request, queryset):
    call_execute_job(modeladmin, request, queryset, job_function=get_time_now)
    return
ac_get_time_now.short_description = "Pintar la hora actual"


#----------------------------------

def save_records(**kwargs):
    """
        Salvar los registros indicados en el parámetro queryset
    """
    queryset = kwargs.get('queryset', None)
    count = 0
    records = []
    for obj in queryset:
        if not obj.locked:
            count +=1
            obj.save()
            records.append(obj)
    response = {
        'message': 'Grabados  %s / %s registros.' % (count,queryset.count()),
        'level': messages.SUCCESS,
        'data': records
    }
    return response
save_records.short_description = "Save Records"
save_records.kwargs = 'queryset'
save_records.response = 'message, level, data'


def ac_save_records(modeladmin, request, queryset):
    """
        Salvar los registros seleccionados
    """
    qs = queryset.filter(locked=True)
    saved_objs = call_execute_job(modeladmin, request, qs, job_function=save_records)
    return
ac_save_records.short_description = "call Save Records"

#---------------------------

def delete_records(**kwargs):
    """
        Borrar los registros indicados en el parámetro queryset
    """
    queryset = kwargs.get('queryset', None)
    count = 0
    records = [NONE]
    for obj in queryset:
        if not obj.locked:
            count += 1
            obj.delete()
            records.append(obj)
    response = {
        'message': 'Borrados  %s / %s registros.' % (count,queryset.count()),
        'level': messages.SUCCESS,
        'data': records
    }
    return response
delete_records.short_description = "Delete Recods"
delete_records.kwargs = 'queryset'
save_records.response = 'message, level, data'

def ac_delete_records(modeladmin, request, queryset):
    """
        Salvar los registros seleccionados
    """
    
    call_execute_job(modeladmin, request, queryset, job_function=delete_records)
    # kwargs = {'queryset': queryset}
    # response = save_records(**kwargs)
    # modeladmin.message_user(request, response['message'], response['level'])
    return
ac_delete_records.short_description = "call Delete Records"

