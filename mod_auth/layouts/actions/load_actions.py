import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _

from mod_auth.adjango.models import Site 
from ..models import Layout


def ac_load_layout(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.parent and not obj.locked:
            load_layout(obj)
            message = "Función %s realizada" % obj.alias
            modeladmin.message_user(request, message, level=messages.SUCCESS)
        else:
            message = _("el layout:%s, %s no se carga porque no es raiz o está bloqueado") % (obj.id, obj.name)
            modeladmin.message_user(request, message, level=messages.warning)
        return
ac_load_layout.short_description = "Crear Layout con sus Componentes"



def load_layout(obj):
    data = get_DATA_LAYOUT()
    site = obj.site

    try:
        l0 = Layout.objects.get(site=site, level=0, pos=None)
            # root_alias=None, last_alias=obj.alias)
    except Layout.DoesNotExist:
        l0 = Layout(site=site, last_alias=obj.alias)
        l0.sort = ""
        l0.name = data[0][2]
        l0.save()
    #-----------
    # import pdb; pdb.set_trace()
    for data_row in data[1:]:
        pos_parent = data_row[0][:-3]
        sort = data_row[0][-2:]
        # grade = data_row[1]
        last_alias = data_row[1]
        active = data_row[2]
        mark = data_row[3]
        mark_i18n = data_row[4]
        name = data_row[5]
     
        if len(data_row)>6 and data_row[6]:
            note = data_row[6]
        else:
            note = ""
        try:
            lp = Layout.objects.get(site=site, root_alias=obj.alias, pos=pos_parent)
        except Layout.DoesNotExist:
            print("layout_pos")
            import pdb; pdb.set_trace()
        try:
            lx = Layout.objects.get(site=site, parent=lp, sort=sort, last_alias=last_alias)
            if not obj.replace:
                continue
        except Layout.DoesNotExist:
            lx = Layout(site=site, parent=lp, sort=sort, last_alias=last_alias)
            
        lx.active = active
        if mark:
            lx.mark = mark
            lx.internal = False
        else:
            lx.internal = True
        if mark_i18n:
            lx.mark_i18n = mark_i18n
            lx.replace = True
        else:
            lx.replace = False
        if name:
            lx.name = name
        else:
            lx.name = last_alias
        if note:
            lx.note = note
        lx.save()
        if mark_i18n:
            lx.create_i18n()

    return


#-----------------------
def get_DATA_LAYOUT():
    return [
    # pos=parent+sort, grade, active, mark, has_mark_i18n, name, note, tags
    ['', 'asinex', 1,'', '', ''],
    #---------------------------------------------
    ['_01', 'appBar', 1,'', '', ''],
    ['_01_01', 'logo', 1,'', '', ''],
    ['_01_02', 'navbar', 1,'', '', ''],
    ['_01_02_01', 'navbar1', 1,'', '', ''],
    ['_01_02_01_01', 'nb1language', 1, '', 'innerHTML__name', 'LANGUAGES'],
    ['_01_02_01_02', 'nb1menulan', 1,'loadLanguages', '', ''],
    ['_01_02_01_02_01', 'nb1de', 1,'', '', 'German'],
    ['_01_02_01_02_02', 'nb1en', 1,'', '', 'English'],
    ['_01_02_01_02_03', 'nb1es', 1,'', '', 'Spanish'],
    ['_01_02_01_02_04', 'nb1fr', 1,'', '', 'France'],
    ['_01_02_02', 'navbar2', 1,'', 'innerHTML__name', 'ABOUT'],
    ['_01_02_03', 'navbar3', 1,'', 'innerHTML__name', 'WORK'],
    ['_01_02_04', 'navbar4', 1,'', 'innerHTML__name', 'TEAM'],
    ['_01_02_05', 'navbar5', 1,'', 'innerHTML__name', 'CONTACT'],
    #-----------------------------------
    ['_02', 'sideBar' ,1, '', '', ''],
    ['_02_00', 'sidebar0',1, '', 'innerHTML__name', 'CLOSE'],
    ['_02_01', 'sidebar1', 1, '', '', ''],
    ['_02_01_01', 'sb1language', 1, '', 'innerHTML__name', 'LANGUAGES'],
    ['_02_01_02', 'sb1menulan', 1, '', '', ''],
    ['_02_01_02_01', 'sb1de', 1, '', '', 'German'],
    ['_02_01_02_02', 'sb1en', 1, '', '', 'English'],
    ['_02_01_02_03', 'sb1es', 1, '', '', 'Spanish'],
    ['_02_01_02_04', 'sb1fr', 1, '', '', 'France'],
    ['_02_02', 'sidebar2', 1, '', 'innerHTML__name', 'ABOUT'],
    ['_02_03', 'sidebar3', 1, '', 'innerHTML__name', 'WORK'],
    ['_02_03_01', 'sb3menu_work3', 1, 'loadSubMenu', '', 'WORK'],
    ['_02_04', 'sidebar4', 1, '', 'innerHTML__name', 'TEAM'],
    ['_02_05', 'sidebar5', 1, '', 'innerHTML__name', 'CONTACT'],
    #--------------------------------------------
    ['_03', 'slideShow', 1, '', '', ''],
    ['_03_01', 'slide1', 1, '', '', ''],
    ['_03_02', 'slide2', 1, '', '', ''],
    ['_03_03', 'slide3', 1, '', '', ''],
    ['_03_04', 'slide4', 1, '', '', ''],
    ['_03_05', 'slide5', 1, '', '', ''],
    #----------------------------------
    ['_04', 'about', 1, '', '', ''],
    ['_04_01', 'about1', 1, '', 'innerHTML__name', 'ABOUT THE COMPANY'],
    ['_04_02', 'about2', 1, '', 'innerHTML__name', 'Key features of our company'],
    ['_04_03', 'about3', 1, '', 'loadDashboard', 'ABOUT US'],
    ['_04_03_01', 'about3-1', 1, '', 'innerHTML__content', 'ABOUT WORK1: leer más'],
    ['_04_03_02', 'about3-2', 1, '', '', 'ABOUT2'],
    ['_04_03_03', 'about3-3', 1, '', '', 'ABOUT3'],
    ['_04_03_04', 'about3-4', 1, '', '', 'ABOUT4'],
    ['_04_03_05', 'about3-5', 1, '', '', 'ABOUT5'],
    ['_04_03_06', 'about3-6', 1, '', '', 'ABOUT6'],
    ['_04_03_07', 'about3-7', 1, '', '', 'ABOUT7'],
    ['_04_03_08', 'about3-8', 1, '', '', 'ABOUT8'],
    ['_04_03_09', 'about3-9', 1, '', '', 'ABOUT9'],
    ['_04_04', 'about4', 1, '', '', ''],
    ['_04_05', 'about5', 1, '', '', ''],
    #---------------------------------------
    ['_05', 'work', 1, '', '', ''],
    ['_05_01', 'work1', 1, '', 'innerHTML__name', 'ABOUT OUR SERVICES'],
    ['_05_02', 'work2', 0, '', 'innerHTML__name', 'Key features of our services'],
    ['_05_03', 'work3', 1, '', '', ''],
    ['_05_03_01', 'work3-1', 1, '', 'innerHTML__content', 'Legal Consultancy', 'work3' ],
    ['_05_03_02', 'work3-2', 1, '', 'innerHTML__content', 'Accounting and Tax', 'work3'],
    ['_05_03_03', 'work3-3', 1, '', 'innerHTML__content', 'ECCO', 'work3'],
    ['_05_03_04', 'work3-4', 1, '', 'innerHTML__content', 'Other Services', 'work3'],
    ['_05_03_05', 'work3-5', 1, '', 'innerHTML__content', 'Plus Information', 'work3'],
    ['_05_03_06', 'work3-6', 1, '', '', ''], 
    ['_05_03_07', 'work3-7', 1, '', '', ''],
    ['_05_03_08', 'work3-8', 1, '', '', ''],
    ['_05_03_09', 'work3-9', 1, '', '', ''],
    #------------------------------
    ['_06', 'extra', 0, '', '', ''],
    #------------------------
    ['_07', 'team', 1, '', '', ''],
    ['_07_01', 'team1', 1, '', 'innerHTML__name', 'ABOUT THE TEAM'],
    ['_07_02', 'team2', 1, '', 'innerHTML__name', 'Key features of our team'],
    ['_07_03', 'team3', 1, '', '', ''],
    ['_07_03_01', 'team3-1', 1, '', '', 'Andrea', ],
    ['_07_03_01_01', 'team3-1-1', 1, '', '', 'Picture',],
    ['_07_03_01_02', 'team3-1-2', 1, '', '', 'Andrea Royen', ],
    ['_07_03_01_03', 'team3-1-3', 1, '', 'innerHTML__name', 'Job',],
    ['_07_03_01_04', 'team3-1-4', 0, '', '', 'Email', ],
    ['_07_03_01_05', 'team3-1-5', 1, '', 'innerHTML__name', 'Profile', ],
    ['_07_03_02', 'team3-2', 1, '', '', 'Fran', ],
    ['_07_03_02_01', 'team3-2-1', 1, '', '', 'Picture', ],
    ['_07_03_02_02', 'team3-2-2', 1, '', 'innerHTML__name', 'Fran M. González Vigo', ],
    ['_07_03_02_03', 'team3-2-3', 1, '', 'innerHTML__name', 'Job', ],
    ['_07_03_02_04', 'team3-2-4', 0, '', '', 'Email', ],
    ['_07_03_02_05', 'team3-2-5', 1, '', 'innerHTML__name', 'Profile', ],
    ['_07_03_03', 'team3-3', 1, '', '', 'Pilar', ],
    ['_07_03_03_01', 'team3-3-1', 1, '', '', 'Picture', ],
    ['_07_03_03_02', 'team3-3-2', 1, '', 'innerHTML__name', 'Pilar Jiménez Girela', ],
    ['_07_03_03_03', 'team3-3-3', 1, '', 'innerHTML__name', 'Job', ],
    ['_07_03_03_04', 'team3-3-4', 0, '', '', 'Email', ],
    ['_07_03_03_05', 'team3-3-5', 1, '', 'innerHTML__name', 'Profile',],
    ['_07_03_04', 'team3-4', 1, '', '', 'Samuel', ],
    ['_07_03_04_01', 'team3-4-1', 1, '', '', 'Picture',],
    ['_07_03_04_02', 'team3-4-2', 1, '', 'innerHTML__name', 'José Samuel Ruíz Del Castillo', ],
    ['_07_03_04_03', 'team3-4-3', 1, '', 'innerHTML__name', 'Job', ],
    ['_07_03_04_04', 'team3-4-4', 0, '', '', 'Email', ],
    ['_07_03_04_05', 'team3-4-5', 1, '', 'innerHTML__name', 'Profile', ],
    ['_07_03_05', 'team3-5', 1, '', '', 'Monique', ],
    ['_07_03_05_01', 'team3-5-1', 1, '', '', 'Picture',],
    ['_07_03_05_02', 'team3-5-2', 1, '', 'innerHTML__name', 'Monique Royen', ],
    ['_07_03_05_03', 'team3-5-3', 1, '', 'innerHTML__name', 'Job', ],
    ['_07_03_05_04', 'team3-5-4', 0, '', '', 'Email', ],
    ['_07_03_05_05', 'team3-5-5', 1, '', 'innerHTML__name', 'Profile', ],
    ['_07_03_06', 'team3-6', 1, '', '', 'Esperanza', ], 
    ['_07_03_06_01', 'team3-6-1', 1, '', '', 'Picture', ],
    ['_07_03_06_02', 'team3-6-2', 1, '', 'innerHTML__name', 'Esperanza Rodríguez Mendoza', ],
    ['_07_03_06_03', 'team3-6-3', 1, '', 'innerHTML__name', 'Job', ],
    ['_07_03_06_04', 'team3-6-4', 0, '', '', 'Email', ],
    ['_07_03_06_05', 'team3-6-5', 1, '', 'innerHTML__name', 'Profile',],
    ['_07_03_07', 'team3-7', 1, '', '', ''],
    ['_07_03_08', 'team3-8', 1, '', '', ''],
    ['_07_03_09', 'team3-9', 1, '', '', ''],
    #-----------------------------------------
    ['_08', 'contact', 1, '', '', ''],
    ['_08_01', 'contact1', 1, '', 'innerHTML__name', 'CONTACT US'],
    ['_08_02', 'contact2', 1, '', 'innerHTML__name', 'How you can contact us'],
    ['_08_03', 'contact3', 1, '', '', 'logo'],
    ['_08_04', 'contact4', 1, '', '', 'address'],
    ['_08_05', 'contact5', 1, '', '', 'google maps location'],
    #----------------------------------
    ['_09', 'footer', 1, '', '', ''],
    ['_09_01', 'footer1', 1, '', 'innerHTML__name', 'To the top'],
    ['_09_02', 'footer2', 0, '', 'innerHTML__name', 'Powered by '],
    ['_09_03', 'footer3', 0, '', 'innerHTML__name', 'Legal Notice'],
    ['_09_03_00', 'footer30', 0, '', 'innerHTML__content', 'Legal Notice'],
    ['_09_04', 'footer4', 0, '', 'innerHTML__name', 'Privacy Policy'],
    ['_09_04_00', 'footer40', 0, '', 'innerHTML__content', 'Privacy Policy'],
    ['_09_05', 'footer5', 0, '', 'innerHTML__name', 'Cookies Policy'],
    ['_09_05_00', 'footer50', 0, '', 'innerHTML__content', 'Cookies Policy'],
    
]

