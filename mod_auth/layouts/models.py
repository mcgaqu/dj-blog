
from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import Group, User
# from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import  gettext_lazy as _
from django.utils.html import format_html
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from mod_admin.main1.models.modelbase import ModelBase, ModelAuxBase
from mod_admin.main1.models.modeltree import ModelTree, ModelTree1
from mod_admin.utils.base import get_site
# from mod_auth.companies.models import Company


#--------------------------
# Layout
#-----------------------------------

class Component(ModelTree1):
    site = models.ForeignKey(Site,  on_delete=models.CASCADE,
                                null=True, blank=True)
    front = models.CharField(max_length=250, null=True, blank=True)

    class Meta(ModelTree1.Meta):
        verbose_name= _("Component")
        verbose_name_plural= _("1. Components")
        unique_together= (('site','alias'),)

    def __str__(self):
        return self.alias

    def save(self, *args, **kwargs):
        if not self.site:
            self.site = get_site(settings.SITE_ID)
        return super().save(*args, **kwargs)


# class ComponentProp(ModelBase):
#     component = models.ForeignKey(Component, on_delete=models.CASCADE, 
#                                     null=True, blank=True)
                                
#     class Meta(ModelBase.Meta):
#         verbose_name = _('Component Property')
#         verbose_name_plural = _('2. Component Properties')
#         unique_together= (('component','alias'),)

#     def MC_grade(self):
#         if self.component:
#             return "%s" % self.component.grade
#         return None

class Layout(ModelTree1):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, 
                                    null=True, blank=True)
    front = models.CharField(max_length=250, null=True, blank=True)

    mark_i18n = models.CharField(max_length=250, null=True, blank=True)

    content = RichTextField(null=True, blank=True)

    comp = models.ForeignKey(Component,  on_delete=models.CASCADE,
                                null=True, blank=True)   
    class Meta(ModelTree1.Meta):
        verbose_name = _('Template')
        verbose_name_plural = _('3. Templates')
        unique_together= (('site', 'pos'),)
        ordering = ('site','pos',)

    def __str__(self):
        return "%s" % (self.alias)
            

    def MH_content(self):
        if not self.content:
            return ""
        return format_html(self.content)

    def ME_num_i18n(self):
        return self.layouti18n_set.count()
    ME_num_i18nshort_description = _("Nº I18n")

    def MC_prefix0_grade(self):
        if not self.grade:
            return ""
        return self.grade.split('-')[0]

    def save(self, *args, **kwargs):
        if not self.site:
            self.site = get_site(settings.SITE_ID)
        return super().save(*args, **kwargs)


    def expand_component_layout(self):
        try:
            # comp = Component.objects.get(biz=self.biz, alias=self.grade)
            # self.comp = comp
            # s = self.comp.componentprop_set.all()
            comps = Component.objects.filter(site=self.site, alias__startswith=self.component.alias)
            if comps:
                for comp in comps:
                    try:
                        lay = Layout.objects.get(site=self.site, parent=self, alias=comp.alias)
                    except Layout.DoesNotExist:
                        lay = Layout(site=self.site, parent=self, alias=comp.alias)
                        lay.grade = comp.name
                        lay.save()

        except Component.DoesNotExist:
            pass
        return    

    def create_i18n(self):
        if not self.replace:
            return
        # TODO! obtener de configuracion de la empresa. cargar en loadCompanyProp
        lans = ['en', 'fr', 'de', 'es']
        count = 0
        for lan in lans:
            aliasId = "%s__%s" % (self.alias, lan)
            count +=1
            try:
                # reg = LayoutI18n.objects.get(alias=aliasId)
                reg = LayoutI18n.objects.get(layout=self, last_alias=lan)
                if self.locked or reg.locked:
                    continue
            except LayoutI18n.DoesNotExist:
                reg = LayoutI18n(layout=self, last_alias=lan)
            reg.grade = self.last_alias
            reg.sort = lan
            reg.name = "%s in %s" % (self.name, lan.upper())
            reg.mark = self.mark_i18n
            # reg.note = Traducir a %s %s" % (
            #        lan.upper(), self.note)
            reg.content = "Traducir a %s %s" % (
                    lan.upper(), self.content)
            reg.save()
        return


class LayoutI18n(ModelBase):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, 
                                    null=True, blank=True)
    layout_root_alias = models.CharField(max_length=250, null=True, blank=True)
    last_alias = models.CharField(max_length=50, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)


    content = RichTextField(null=True, blank=True)


    class Meta(ModelBase.Meta):
        verbose_name = _('Traductor')
        verbose_name_plural = _('4. Traductores')
        unique_together= (('layout', 'alias'),)
        ordering = ('sort',)

    def MH_content_ini(self):
        texto = ""
        accion = 'MODIFICAR' if self.content else "AÑADIR"
        
        if self.mark and '__content' in self.mark:
            texto = '<span>Pulse Intro para %s: </span>' % accion
        return format_html(texto)
    MH_content_ini.short_description = 'Editar Contenido'

    def MH_content(self):
        if not self.content:
            return ""
        return format_html(self.content)
    MH_content.short_description = 'Content'


    def MC_language(self):
        lans = {
            'de': 'GERMAN',
            'en': 'ENGLISH',
            'es': 'SPANISH',
            'fr': 'FRANCE'
        }
        if self.last_alias in lans.keys():
            return lans[self.last_alias]
        else:
            return ""
    MC_language.short_description = 'Idioma'
    MC_language.admin_order_field = 'last_alias'

    def MC_layout_name(self):
        if self.layout:
            return self.layout.name
        return ""
    MC_layout_name.short_description = 'Texto Base'

    def MC_layout_grade(self):
        if self.layout:
            return self.layout.grade
        return ""

    def MC_layout_sort(self):
        if self.layout:
            return self.layout.sort
        return ""

    def MC_layout_alias(self):
        if self.layout:
            return self.layout.alias
        return ""

    def MC_layout_pos(self):
        if self.layout:
            return self.layout.pos
        return ""

    def save(self, *args, **kwargs):
        if self.layout:
            self.alias = "%s__%s" % (self.layout.alias, self.last_alias)
            self.pos = "%s__%s" % (self.layout.pos, self.sort)
            self.layout_root_alias = self.layout.root_alias 
        super().save(*args, **kwargs)

