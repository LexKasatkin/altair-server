from .models import Flat
from django_filters import rest_framework as filters

class FlatFilter(filters.FilterSet):
    class Meta:
        model = Flat
        fields = ['id', 'city', 'wall_material', 'flat_type',
                  'developer', 'district']