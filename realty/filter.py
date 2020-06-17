from .models import Flat, FlatImage
from django_filters import rest_framework as filters

class FlatFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    square = filters.RangeFilter()
    year_of_completion = filters.RangeFilter()
    class Meta:
        model = Flat
        fields = ['id', 'wall_material', 'flat_type',
                  'developer', 'street', 'cost', 'square', 'residential_complex',
                'year_of_completion', 'flat_image', 'quarter']


class FlatImageFilter(filters.FilterSet):
    class Meta:
        model = FlatImage
        fields = ['flat']