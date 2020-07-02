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


class FlatFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    square = filters.RangeFilter()
    house = filters.CharFilter(
        field_name='house',
        lookup_expr='icontains',
        method='filter_house_year_of_completion'
    )

    class Meta:
        model = Flat
        fields = {'id', 'cost', 'square', 'house'}

    def filter_house_year_of_completion(self, queryset, name, value):
        street = Q(house__street__icontains=value)
        year_of_completion = Q(house__year_of_completion__icontains=value)
        return queryset.filter(street | year_of_completion)

class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = ['flat']