from .models import Flat, Album, House,Developer, Street, District
from django_filters import rest_framework as filters
from django.db.models import Q

class DeveloperFilter(filters.FilterSet):
    class Meta:
        model = Developer
        fields = {'id'}


class DistrictFilter(filters.FilterSet):
    class Meta:
        model = District
        fields = {'name'}


class StreetFilter(filters.FilterSet):
    district = DistrictFilter()
    class Meta:
        model = Street
        fields = {'name', 'district'}


class HouseFilter(filters.FilterSet):
    year_of_completion = filters.RangeFilter()
    developer = DeveloperFilter()
    street = StreetFilter()
   
    class Meta:
        model = House
        fields = {'year_of_completion', 'developer', 'street'}


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class FlatFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    square = filters.RangeFilter()
    developer = NumberInFilter(field_name='house__developer', lookup_expr='in')
    wall_material =  NumberInFilter(field_name='house__wall_material', lookup_expr='in')
    street = NumberInFilter(field_name='house__street', lookup_expr='in')
    flat_type = NumberInFilter(field_name='house__flat_type', lookup_expr='in')
    district = NumberInFilter(field_name='house__street__district', lookup_expr='in')

    class Meta:
        model = Flat
        fields = {'id', 'cost', 'square', 'house__developer', 'house__wall_material', 'house__street', 'house__street__district',
                  'house__flat_type'}


class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = ['flat']