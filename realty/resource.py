from import_export import resources
from .models import City, Flat

class CityResource(resources.ModelResource):

    class Meta:
        model = City

class FlatResource(resources.ModelResource):
    class Meta:
        model = Flat
        fields = ('house__residential_complex__name', 'house__street__name', 'house__house', 'house__street__district__name',
                  'flat_type__name', 'floor', 'house__max_floor', 'square', 'subject_of_law',
                  'house__wall_material__name', 'cost', 'house__developer__name', 'house__year_of_completion', 'house__quarter',
                  'description',)
        export_order = ('house__residential_complex__name', 'house__street__name', 'house__house', 'house__street__district__name',
                        'flat_type__name', 'floor', 'house__max_floor', 'square', 'subject_of_law',
                  'house__wall_material__name', 'cost', 'house__developer__name', 'house__year_of_completion', 'house__quarter',
                  'description',)