# from .load_actions 
# from mod_admin.main1.actions import ac_save_records
from .biz_actions import ac_create_i18n, ac_expand_component_layout
from .load_actions import ac_load_layout

def get_job_actions():
    return [
        
    ]

def get_call_actions(index=None):
    return [
        ac_create_i18n,
        ac_expand_component_layout
    ]

def get_app_actions(index=None):
    dev = {
		'Layout': [
            ac_load_layout,
			ac_create_i18n,
            # ac_save_records,
		],
		'LayoutI18n':[
			# ac_save_records, # los datos-factor de la hoja de calculo
		],
    }
    if not index:
        return dev
    elif not index in dev.keys():
        return None
    return dev[index]