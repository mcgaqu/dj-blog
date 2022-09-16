# -*- coding: utf-8 -*-

from rest_framework import routers
# from mod_auth.adjango.apis.apirest import UserViewSet, GroupViewSet, SiteViewSet
# from mod_auth.companies.apis.apirest import (
#     CompanyViewSet, CompanyLoadViewSet, CompanyPropViewSet,
#     MenuViewSet, MenuItemViewSet,
# )
# from mod_auth.doctypes.apis.apirest import DocTypeViewSet, DocTypePropViewSet 
from mod_auth.layouts.apis.apirest import LayoutViewSet, LayoutI18nViewSet 



router = routers.DefaultRouter()
#--------------------------------
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'sites', SiteViewSet)
# #-------------------
# router.register(r'companys', CompanyViewSet)
# router.register(r'companyloads', CompanyLoadViewSet)
# router.register(r'companyprops', CompanyPropViewSet)
# router.register(r'menus', MenuViewSet)
# router.register(r'menuitems', MenuItemViewSet)
# #-------------------
# router.register(r'doctypes', DocTypeViewSet)
# router.register(r'doctypeprops', DocTypePropViewSet)
#-------------------
router.register(r'layouts', LayoutViewSet)
router.register(r'layouti18ns', LayoutI18nViewSet)
#--------------------------------
