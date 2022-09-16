from django.conf import settings
from django.contrib import admin
# from django.contrib.auth.models import Group
from mod_admin.main1.options import ModelAdmin1, ModelLin1
# from mod_base.configs.models import Config1, Config2
from .models import Component, Layout, LayoutI18n
from .actions import get_app_actions

#------------------------------
# Component
#------------------------
class ComponentChildLin1(ModelLin1):
    model = Component
    fields = ['sort', 'alias', 'name', 'json', 'active'] # 'name', 'grade', 'sort']



class ComponentAdmin1(ModelAdmin1):
    model = Component
    list_display = ['site', 'alias', 'name', 'grade', 'sort']
    fields = ['alias', 'name', 'grade', 'sort']
    list_filter = ['site', 'active', 'grade']
    inlines = [ComponentChildLin1]

#------------------------------
# Layout
#------------------------

class LayoutI18nAdmin1(ModelAdmin1):
    model = LayoutI18n
    field_labels = {
        'layout': [], # 'parent': [], 'level': [],
        'grade': [], 'alias':[],
        'sort':[], # 'pos': [],
        'layout_root_alias': [],
        'active': [], 'internal': [],
        'replace': [], 'locked':[],
        'mark': [], # 'mark_i18n': [],
        'name': [],'MC_layout_name': [],
        'content': [], 'MH_content': [],
        'MC_layout_grade': [], 'MC_layout_alias': [],
        'MC_layout_sort': [], 'MC_layout_pos': [],
        'MC_language': [], 'MH_content_ini':[]
    }


    list_display = [# 'sort',
        'layout', 'grade', 'MC_layout_name', 'MC_language','name',
                        'MH_content_ini','locked']

    def x_get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display_user
        else:
            return self.list_display_super

    list_display_links = ['grade','MH_content_ini',]

    list_editable = ['name', 'locked' ]

    list_filter = ['sort', 'layout_root_alias', 'locked', 'grade', 'mark', 'active', 
    'layout__site',
    ]
    search_fields = ['grade', 'layout__name', 'sort', 'name', 'content' ]
    ## 'alias', 'name', 'grade','sort', 'pos', 'mark'
    # fields = ['doctype','grade', 'sort', 'alias', 'name', 'mark', 'docfile', 'content',
    #      'active', 'locked', 'MH_content']
    actions = get_app_actions('LayoutI18n')
    

    fieldsets = [
		(None, {
			'fields': [	
                ('layout', 'grade', ),
                # ('alias', 'sort',),                
                ('mark', 'name'),
                # ('active', 'internal'),
				# ('docfile',),
                # ('note',),
                ('content',),
                ('MH_content',)
            ]
		}),
		('Internal', {
			'fields': [	
                # ('layout', 'grade', ),
                ('alias', 'sort',),                
                # ('mark', 'name'),
                ('active', 'internal'),
                ('replace', 'locked'),
				# ('docfile',),
                ('note',),
                # ('content',),
                # ('MH_content',)
            
            ],
            'classes': ['collapse']
		}),  
	]

    readonly_fields = ['alias', 'sort', 'MH_content']

class LayoutI18nLin1(ModelLin1):
    model = LayoutI18n
    fields = ['alias', 'grade', 'mark', 'name', 'active', 'internal',
    # 'note', 'content' 
    ]
    readonly_fields = ['alias', 'grade']
    classes = []

class LayoutChildLin1(ModelLin1):
    model = Layout
    fields = [# 'alias', 
        'grade', 'sort', 'active', 'internal', 'mark', 'name' ]
    classes = []

class LayoutAdmin1(ModelAdmin1):
    model = Layout

    field_labels = {
        'site': [], 'parent': [], 'level': [],
        'grade': [], 'alias':[], 'last_alias':[],
        'sort':[], 'pos': [],
        'root_alias': [],
        'active': [], 'internal': [],
        'replace': [], 'locked':[],
        'mark': [], 'mark_i18n': [],
        'name': [], 'note': [],
        # 'content': [], 'MH_content': [],
        'ME_num_children': [], 
        'ME_num_i18n': []
    }

    list_display = [
        'level', 'pos',
        'site', 'parent', 'sort', 'last_alias', 'mark',
        #'alias',  'grade',  'name',  # 'note', # 'content',
        'active', 'internal', 'locked',
        'ME_num_children', 'replace', 'ME_num_i18n', 
         ]
    list_display_links = ['pos',]
    list_editable = [
        'site','parent', 'sort', 'last_alias', 'mark',

        'active', 'internal', 'replace']
    ordering = ('pos',)
    list_filter = ['root_alias', 'level', 'active', 'internal',
        # 'parent', 'grade',
        'locked', 'replace', ]
    search_fields = ['pos','alias',  
        'grade', 'mark', 'mark_i18n', 'name',]

    actions = get_app_actions('Layout')    
    
    fieldsets = [
		(None, {
			'fields': [	
                ('site', 'parent', 'sort', 'last_alias',),

                'grade', 'alias', 'pos',

                # 'active', 'internal', 'locked', 'replace'),
               ]         
		}), 
        ('Data', {
            'fields': [	
                #'docfile',
    			('mark', 'name', 'mark_i18n'),
                ('note','content'),
 
            ],
            # 'classes': ['collapse']
		}), 
	]
    readonly_fields = ['pos', 'alias']
    inlines = [LayoutChildLin1, LayoutI18nLin1]


if True: # settings.NUM_ADMIN_SITE == "0":
    admin.site.register(Component, ComponentAdmin1)
    admin.site.register(Layout,LayoutAdmin1)
    admin.site.register(LayoutI18n, LayoutI18nAdmin1)


