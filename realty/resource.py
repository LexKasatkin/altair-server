from import_export import resources
from .models import City, Flat

class CityResource(resources.ModelResource):

    class Meta:
        model = City

class FlatResource(resources.ModelResource):

    class Meta:
        model = Flat
        fields = ('address', 'subject_of_law', 'description', 'wall_material', 'city',
                  'district','flat_type','developer','cost','square', 'deadline')
        export_order = ('address', 'district', 'flat_type', 'square', 'subject_of_law',
                  'wall_material','cost','developer','deadline','description')