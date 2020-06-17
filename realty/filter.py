from .models import Flat, Album
from django_filters import rest_framework as filters

class FlatFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    square = filters.RangeFilter()
    year_of_completion = filters.RangeFilter()
    class Meta:
        model = Flat
        fields = ['id', 'wall_material', 'flat_type',
                  'developer', 'street', 'cost', 'square', 'residential_complex',
                'year_of_completion', 'quarter']


class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = ['flat']