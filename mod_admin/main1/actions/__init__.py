from .biz_actions import (
        display_function_name, call_execute_job,
        get_time_now, ac_get_time_now,
        save_records, ac_save_records, 
        delete_records, ac_delete_records,
) 


#--------------------------

def get_job_actions():
    return [
        get_time_now,
        save_records,
        delete_records,
        #--------------------------
        'export_list_pdf',
        'export_list_xls',
    ]

def get_call_actions():
    return [
        ac_get_time_now,
        ac_save_records,
        ac_delete_records,
        
    ]

def get_display_actions():
    return 