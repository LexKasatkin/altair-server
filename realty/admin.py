from django.contrib import admin

# Register your models here.
from realty.models import City, RealtyType, District, FlatType, Developer, WallMaterial, Flat, Street, ResidentialComplex, \
    Image, FlatImage
from import_export.admin import ImportExportModelAdmin
from .resource import CityResource, FlatResource

class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource

class FlatAdmin(ImportExportModelAdmin):
    resource_class = FlatResource

admin.site.register(City, CityAdmin)
admin.site.register(District)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Developer)
admin.site.register(WallMaterial)
admin.site.register(FlatType)
admin.site.register(RealtyType)
admin.site.register(ResidentialComplex)
admin.site.register(Image)
admin.site.register(FlatImage)
admin.site.register(Street)