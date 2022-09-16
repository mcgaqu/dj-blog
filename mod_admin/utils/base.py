from importlib import import_module
import calendar, datetime, decimal
from django.conf import settings





def print_msg(msg):
    # if settings.DEBUG:
    print(msg)
    return

def get_site(id_site=settings.SITE_ID):
    # if not settings.BIZ_ID:
    #     return None

    from django.contrib.sites.models import Site
    try:
        site = Site.objects.get(id=id_site)
    except: #  Cms.DoesNotExist: o no existe la tabla
        site = None
    return site



def get_biz(alias_biz=settings.SITE_NAME):
    # if not settings.BIZ_ID:
    #     return None

    from mod_bpmn.business.models import Biz
    try:
        biz = Biz.objects.get(alias=alias_biz)
    except: #  Cms.DoesNotExist: o no existe la tabla
        biz = None
    return biz


def get_company(alias_emp=settings.SITE_NAME):
    from mod_auth.companies.models import Company
    try:
        company = Company.objects.get(alias=alias_emp)
    except: # Emp.DoesNotExist:
        company = None
    return company

def get_module_attr(mod, attr=None):
    # import pdb; pdb.set_trace()
    try:
        module = import_module(mod)
    except ModuleNotFoundError:
        return (None, None)
    if not attr or not hasattr(module, attr):
        return (module, None)
    attr_module = getattr(module, attr)
    return (module, attr_module)



#------------------------------------

def redondea(numero, redondeo=2, tipo=None, empresa=None):
    if not numero and numero != 0:
        numero = 0
        
    try:
        numero = decimal.Decimal(str(numero))
    except:
        numero = decimal.Decimal(0)
    
    if tipo in ('unidades', 'precios', 'importes',):
        pass
        # redondeo = decimales_parametro_empresa(tipo, empresa)
    elif tipo and tipo.isdigit():
        # el tipo puede llevar el numero de decimales
        redondeo = int(tipo)
    return numero.quantize(decimal.Decimal(10)**(-redondeo), decimal.ROUND_HALF_UP)


def get_dates_from_period(period):
    year = period[0:4]
    if 'D' in period:
        month1 = int(period[7:9])
        month2 = month1
        day1 = int(period[10:12])
        day2 = day1
    elif 'M' in period:
        month1 = int(period[7:9])
        month2 = month1
        day1 = 1
        day2 = calendar.monthrange(year, month2)[1]
    elif 'T' in period:
        trimester = int(period[5:6])
        month1 = (trimester-1)*3 +1
        day1 = 1
        month2 = month1+2
        day2 = calendar.monthrange(year, month2)[1]
    else:
        month1 = 1
        day1 = 1
        month2 = 12
        day2 = 31
    date1 = datetime.date(year, month1, day1)
    date2 = datetime.date(year, month2, day2)
    return (date1, date2)




def get_apirest_fields(model):
    # import pdb; pdb.set_trace()
    fields = model._meta.concrete_fields
    # dev = [x.name for x in fields]
    dev = ['id', 'url']
    for field in fields:
        dev.append(field.name)
        if field.many_to_one:
            dev.append("%s_id" % field.name)# dev.append(field.name)
        # print(field.name)
    # print(dev)
    return dev
