from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .filter import FlatFilter

from realty.models import City, District, RealtyType, FlatType, Developer, Flat, \
    WallMaterial, Street, Image, ResidentialComplex
from realty.serializer import CitySerializer, RealtyTypeSerializer, DistrictSerializer, FlatTypeSerializer, \
    WallMaterialSerializer, DeveloperSerializer, FlatSerializer, StreetSerializer, ResidentialComplexSerializer, \
    ImageSerializer


class FlatListView(generics.ListAPIView):
   queryset = Flat.objects.all()
   serializer_class = FlatSerializer
   filter_backends = (DjangoFilterBackend,)
   filterset_class = FlatFilter

class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"cities": serializer.data})


class DistrictView(APIView):
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response({"districts": serializer.data})


class FlatTypeView(APIView):
    def get(self, request):
        flat_types = FlatType.objects.all()
        serializer = FlatTypeSerializer(flat_types, many=True)
        return Response({"flat_types": serializer.data})


class DeveloperView(APIView):
    def get(self, request):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response({"developers": serializer.data})


class WallMaterialView(APIView):
    def get(self, request):
        wall_materials = WallMaterial.objects.all()
        serializer = WallMaterialSerializer(wall_materials, many=True)
        return Response({"wall_materials": serializer.data})


class FlatView(APIView):
    def get(self, request):
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True)
        return Response({"flats": serializer.data})


class RealtyTypeView(APIView):
    def get(self, request):
        realty_types = RealtyType.objects.all()
        serializer = RealtyTypeSerializer(realty_types, many=True)
        return Response({"realty_types": serializer.data})


class StreetView(APIView):
    def get(self, request):
        streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response({"streets": serializer.data})


class ResidentialComplexView(APIView):
    def get(self, request):
        residential_complexes = ResidentialComplex.objects.all()
        serializer = ResidentialComplexSerializer(residential_complexes, many=True)
        return Response({"residential_complexes": serializer.data})


class ImageView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response({"images": serializer.data})