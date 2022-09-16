from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mod_admin.main1.models.modelbase import ModelBase
# from mod_admin.main1.models.modeltree import ModelTree
# from mod_auth.doctypes.models import ModelDocument





class ModelRel1(ModelBase):

    """
    Relacion genérica de documentos procesados por grafos
    Faltaría indicar la unidad y cantidad de la relacion: ??? 

    """

    # owner = models.ForeignKey('OwnerModel', on_delete=models.CASCADE, 
    #                                 null=True, blank=True)





    # model_rel =models.ForeignKey('BizModel')

    # alias_rel =models.models.CharField()

    ctt1= models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                related_name='%(class)ss_ctt1',
                                   help_text='Tipo de Centro de Coste: cliente, proyecto, conjunto,.. ',
                                   null=True, blank=True)
    id1 = models.PositiveIntegerField(null=True, blank=True,
                                   help_text='Centro de Coste',)
    
    obj1 = GenericForeignKey('ctt1', 'id1')

    
    
    class Meta(ModelBase.Meta):
        abstract = True
        verbose_name = "Fix-Generic Relation"
        verbose_name_plural = "Fix-Generic Relations"
        unique_together = (('ctt1', 'id1'),)
        
    def obj1_alias(self):
        # import pdb; pdb.set_trace()
        if hasattr(self, 'alias'):
            return self.obj1.alias
        else:
            return ''

    def save(self, *args, **kwargs):
        # calcular ctt1 y id1 a apartir de model_rel y alias_rel
        # ctt1 = --
        # id1 = ---
        return super().save(*args, **kwargs)



class ModelRel2(ModelRel1):

    """
    Relacion genérica de documentos procesados por grafos
    Faltaría indicar la unidad y cantidad de la relacion: ??? 
    """
    
    ctt2 = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                related_name='%(class)ss_ctt2',
                                    help_text='Tipo de Causa Coste: parte, compra,..',
                                    null=True, blank=True)
    id2 = models.PositiveIntegerField(null=True, blank=True,
                                    help_text='Causa de Coste')
    obj2 = GenericForeignKey('ctt2', 'id2')
    
    class Meta(ModelRel1.Meta):
        abstract = True
        verbose_name = "Generic Relation"
        verbose_name_plural = "Generic Relations"
        unique_together = (('ctt1', 'id1', 'ctt2', 'id2'),)
        

    def obj2_alias(self):
        # import pdb; pdb.set_trace()
        if hasattr(self, 'alias'):
            return self.obj2.alias
        else:
            return ''




#--------------------------
# Relations
#-----------------------------------
# class Relationx(ModelRel2):


#     class Meta(ModelRel2.Meta):
#         # abstract = True
#         verbose_name = "Generic Relation"
#         verbose_name_plural = "Generic Relations"
#         unique_together = (('ctt1', 'id1', 'ctt2', 'id2'),)


