from rest_framework import serializers
from .models import Album, Street, District, Flat, City, House
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = District
        fields = '__all__'


class FlatTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=60)


class DeveloperSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=60)


class WallMaterialSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=60)


class RealtyTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=60)


class StreetSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    class Meta:
        model = Street
        fields = '__all__'


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)


class ResidentialComplexSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=100)


class HouseSerializer(serializers.ModelSerializer):
    street = StreetSerializer(read_only=True)
    wall_material = WallMaterialSerializer(read_only=True)
    developer = DeveloperSerializer(read_only=True)
    residential_complex = ResidentialComplexSerializer(read_only=True)
    main_image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)

    class Meta:
        model = House
        fields = '__all__'


class FlatSerializer(serializers.ModelSerializer):
    flat_type = serializers.CharField(read_only=True, source='flat_type.name')
    layout = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    layout_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    layout_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    city = serializers.CharField(read_only=True, source='house.street.district.city.name')
    district = serializers.CharField(read_only=True, source='house.street.district.name')
    street = serializers.CharField(read_only=True, source='house.street.name')
    house = serializers.CharField(read_only=True, source='house.house')
    flat = serializers.CharField(read_only=True)
    wall_material = serializers.CharField(read_only=True, source='house.wall_material')
    developer = serializers.CharField(read_only=True, source='house.developer')
    residential_complex = serializers.CharField(read_only=True, source='house.residential_complex')
    year_of_completion = serializers.IntegerField(read_only=True, source='house.year_of_completion')
    quarter = serializers.CharField(read_only=True, source='house.quarter')
    latitude = serializers.FloatField(read_only=True, source='house.latitude')
    longitude = serializers.FloatField(read_only=True, source='house.longitude')
    
    class Meta:
        model = Flat
        fields = '__all__'


class FlatDetailsSerializer(serializers.ModelSerializer):
    flat_type = serializers.CharField(read_only=True, source='flat_type.name')
    layout = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    layout_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    layout_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    main_image_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)
    city = serializers.CharField(read_only=True, source='house.street.district.city.name')
    district = serializers.CharField(read_only=True, source='house.street.district.name')
    street = serializers.CharField(read_only=True, source='house.street.name')
    house = serializers.CharField(read_only=True, source='house.house')
    flat = serializers.IntegerField(read_only=True)
    wall_material = serializers.CharField(read_only=True, source='house.wall_material')
    developer = serializers.CharField(read_only=True, source='house.developer')
    residential_complex = serializers.CharField(read_only=True, source='house.residential_complex')
    house_main_image = serializers.ImageField(read_only=True, source='house.main_image', allow_empty_file=True, use_url=False)
    house_main_image_big = serializers.ImageField(read_only=True, source='house.main_image_big', allow_empty_file=True, use_url=False)
    house_main_image_thumbnail = serializers.ImageField(read_only=True, source='house.main_image_thumbnail', allow_empty_file=True, use_url=False)
    max_floor = serializers.CharField(read_only=True, source='house.max_floor')
    year_of_completion = serializers.IntegerField(read_only=True, source='house.year_of_completion')
    quarter = serializers.CharField(read_only=True, source='house.quarter')
    latitude = serializers.FloatField(read_only=True, source='house.latitude')
    longitude = serializers.FloatField(read_only=True, source='house.longitude')

    class Meta:
        model = Flat
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    flat = FlatSerializer(read_only=True)


    class Meta:
        model = Album
        fields = '__all__'
