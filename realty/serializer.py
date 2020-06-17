from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=60)


class DistrictSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=60)
    city = serializers.CharField(max_length=60)


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


class StreetSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    district = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=60)


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    flat = serializers.CharField(max_length=60)
    name = serializers.CharField(max_length=60)
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)


class ResidentialComplexSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=100)


class FlatSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    subject_of_law = serializers.CharField(max_length=30)
    description = serializers.CharField()
    wall_material = serializers.CharField(max_length=60)
    city = serializers.CharField(max_length=60)
    district = serializers.CharField(max_length=60)
    street = serializers.CharField(max_length=60)
    flat_type = serializers.CharField(max_length=60)
    developer = serializers.CharField(max_length=60)
    cost = serializers.IntegerField()
    square = serializers.FloatField()
    deadline = serializers.CharField(max_length=60)
    photo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    address=serializers.CharField()
    realty_type=serializers.CharField(max_length=60)
    residential_complex = serializers.CharField(max_length=60)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
