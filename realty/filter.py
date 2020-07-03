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
    house = filters.CharFilter(method='filter_by_house')

    class Meta:
        model = Flat
        fields = {'id', 'cost', 'square', 'house'}

    def filter_by_house(self, queryset, name, value):
        developer = Developer.objects.filter(developer__in=value)
        wall_material= WallMaterial.objects.filter(wall_material__in=value)
        street = Street.objects.filter(street__in=value)
        house = House.objects.filter(developer__in=developer).filter(street__in=street).filter(wall_material__in=wall_material)
        return queryset.filter(house__in=house)
        

class AlbumFilter(filters.FilterSet):
    class Meta:
        model = Album
        fields = ['flat']