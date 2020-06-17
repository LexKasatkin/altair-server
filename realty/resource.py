from import_export import resources
from .models import City, Flat

class CityResource(resources.ModelResource):

    class Meta:
        model = City

class FlatResource(resources.ModelResource):

    class Meta:
        model = Flat
        fields = ('street', 'subject_of_law', 'description', 'wall_material',
                'flat_type','developer','cost','square')
        export_order = ('street', 'flat_type', 'square', 'subject_of_law',
                  'wall_material','cost','developer','description')