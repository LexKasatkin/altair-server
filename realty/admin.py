from django.contrib import admin

# Register your models here.
from realty.models import City, District, Image, Flat, Developer, SubjectOfLaw, WallMaterial, Record

admin.site.register(City)
admin.site.register(District)
admin.site.register(Image)
admin.site.register(Flat)
admin.site.register(Developer)
admin.site.register(SubjectOfLaw)
admin.site.register(WallMaterial)
admin.site.register(Record)