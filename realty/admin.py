from django.contrib import admin

# Register your models here.
from realty.models import City, District, FlatType, Developer, WallMaterial, Flat

admin.site.register(City)
admin.site.register(District)
admin.site.register(Flat)
admin.site.register(Developer)
admin.site.register(WallMaterial)
admin.site.register(FlatType)