from rest_framework import serializers
from .models import Album, Street, District, Flat, City
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
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)


class ResidentialComplexSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=100)


class FlatDetailsSerializer(serializers.ModelSerializer):
    street = StreetSerializer(read_only=True)
    wall_material = WallMaterialSerializer(read_only=True)
    flat_type = FlatTypeSerializer(read_only=True)
    developer = DeveloperSerializer(read_only=True)
    realty_type = RealtyTypeSerializer(read_only=True)
    residential_complex = ResidentialComplexSerializer(read_only=True)
    layout = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    main_image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    layout_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    main_image_big = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    layout_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    main_image_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = Flat
        fields = '__all__'


class FlatSerializer(serializers.ModelSerializer):
    flat_type = FlatTypeSerializer(read_only=True)
    street = StreetSerializer(read_only=True)
    layout = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    main_image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    layout_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    main_image_thumbnail = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = Flat
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    flat = FlatSerializer(read_only=True)
    class Meta:
        model = Album
        fields = ('__all__')
