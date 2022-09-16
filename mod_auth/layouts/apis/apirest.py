# -*- coding: utf-8 -*-

from rest_framework import serializers, generics, viewsets
from ..models import Component, Layout, LayoutI18n

#------------------------
# Component
#------------------------
class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ['url', 'id', 'biz', 'alias', 'name']
        
 

class ComponentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Component.objects.all().order_by('alias')
    serializer_class = ComponentSerializer



#--------------------------
# Layout
#-------------------------
class LayoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layout
        fields = ['url', 'id',
            'site', 'parent', 'level', 
            'grade', 'alias', 'last_alias',
            'sort', 'pos',
            'active', 'internal',
            'replace', 'locked',
            'mark', 'mark_i18n',
            'name', 'note',
            # 'content', 'MH_content',
            'name', 'note',
            'ME_num_children',
            'ME_num_i18n',
            'MC_prefix0_grade',
        ]
        # fields = ['url', 'id', 'site', 'alias', 'name']
        
 

class LayoutViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Layout.objects.all().order_by('pos')
    serializer_class = LayoutSerializer

    filterset_fields = ['active', 'internal', 'pos', 'alias', 'last_alias', 'note', # 'MC_prefix0_grade', 
        'root_alias', 'grade', 'sort', 'level', 'mark', 'replace', 'locked']

    search_fields = ['pos', 'alias', 'grade', 'last_alias', 'root_alias', 
                        'MC_prefix0_grade', 'note',
                        'mark', 'mark_i18n', 'name',] # , 'typedoc__name'

    ordering_fields = ['pos', 'alias', 'mark', 'mark_i18n', 'name']
    ordering = ['pos']


class LayoutI18nSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LayoutI18n
        fields = ['url', 'id', 'layout_root_alias', 
            'layout','grade', 'sort', 'alias', 'name', 'mark', 'last_alias', # 'docfile', 
            'content', 'MC_layout_alias','MC_layout_grade', 'MC_layout_pos',
            'active', 'internal', 'locked', 'MH_content', 'note'

        ]
        # fields = ['url', 'id', 'layout', 'alias', 'name']
        
 

class LayoutI18nViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = LayoutI18n.objects.all().order_by('layout', 'alias')
    serializer_class = LayoutI18nSerializer

    filterset_fields = ['alias','grade', 'sort', 'mark', 'note',
        'active', 'internal', 'locked']
    search_fields = ['alias', 'name', 'layout__alias'] # , 'typedoc__name'
    ordering_fields = ['grade', 'sort', 'alias', 'name']
    ordering = ['layout__pos', 'grade']

