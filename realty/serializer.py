from rest_framework import serializers
from .models import Album, Street, District, Flat, City

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


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('__all__')


class ResidentialComplexSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=100)


class FlatSerializer(serializers.ModelSerializer):
    street = StreetSerializer(read_only=True)

    class Meta:
        model = Flat
        fields = '__all__'
