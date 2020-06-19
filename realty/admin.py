from django.contrib import admin

# Register your models here.
from realty.models import City, RealtyType, District, FlatType, Developer, WallMaterial, Flat, Street, ResidentialComplex, \
    Image, Album
from import_export.admin import ImportExportModelAdmin
from .resource import CityResource, FlatResource
from imagekit.admin import AdminThumbnail

class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource

class FlatAdmin(ImportExportModelAdmin):
    resource_class = FlatResource

# @register(Fancy)
# class FancyAdmin(FlatAdmin):
#     list_display = ['name', 'image_display']
#     image_display = AdminThumbnail(image_field='image')
#     image_display.short_description = 'Image'
#     readonly_fields = ['image_display']  # this is for the change form

admin.site.register(City, CityAdmin)
admin.site.register(District)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Developer)
admin.site.register(WallMaterial)
admin.site.register(FlatType)
admin.site.register(RealtyType)
admin.site.register(ResidentialComplex)
admin.site.register(Image)
admin.site.register(Street)
admin.site.register(Album)