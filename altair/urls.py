"""altair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from altair import settings
from realty.views import CityView, FlatTypeView, DeveloperView, WallMaterialView, FlatView

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

class CustomersConfig(AppConfig):
    name = 'Недвижимость'
    verbose_name = _('Недвижимость')

admin.site.index_title = _(u'Джанго администрирование')
admin.site.site_header = _(u'Администрирование сайта')
admin.site.site_title = _(u'Управление сайта')
adminUrl = admin.site.urls
urlpatterns = [
    path('admin/', adminUrl),
    path('', adminUrl),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('realty.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
