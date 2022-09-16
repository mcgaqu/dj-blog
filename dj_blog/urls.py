"""dj_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from .apis.apirest import router

prefix = ''
urlpatterns = [
    path("%sindex1/" % prefix, TemplateView.as_view(template_name='index1.html')),
    path("%sindex2/" % prefix, TemplateView.as_view(template_name='index2.html')),
    #-----------------------------------
    path('%sapirest/' % prefix, include(router.urls)),
    path('%sckeditor/' % prefix, include('ckeditor_uploader.urls')),
    #-------------------------------------
    path('%sadmin/' % prefix, admin.site.urls),

]

if True: # True: # settings.RUNSERVER:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
