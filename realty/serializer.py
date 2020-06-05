from abc import ABC

from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)


class DistrictSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)


class FlatTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)


class DeveloperSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)


class WallMaterialSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)


class FlatSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    description = serializers.CharField()
    cost = serializers.IntegerField()
    square = serializers.IntegerField()
    flat_type = serializers.CharField(max_length=30)
    deadline = serializers.CharField(max_length=30)
    subject_of_law = serializers.CharField(max_length=30)
    photo = serializers.SerializerMethodField()

