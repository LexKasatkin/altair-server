from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.models import City, District, Flat, Developer, Record, Image, SubjectOfLaw, WallMaterial
from realty.serializer import CitySerializer, DistrictSerializer, ImageSerializer, FlatSerializer, \
    SubjectOfLawSerializer, WallMaterialSerializer, DeveloperSerializer, RecordSerializer


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


class ImageView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response({"images": serializer.data})


class FlatView(APIView):
    def get(self, request):
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True)
        return Response({"flats": serializer.data})


class DeveloperView(APIView):
    def get(self, request):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response({"developers": serializer.data})


class SubjectOfLawView(APIView):
    def get(self, request):
        subjectsOfLaw = SubjectOfLaw.objects.all()
        serializer = SubjectOfLawSerializer(subjectsOfLaw, many=True)
        return Response({"subjectsOfLaw": serializer.data})


class WallMaterialView(APIView):
    def get(self, request):
        wall_materials = WallMaterial.objects.all()
        serializer = WallMaterialSerializer(wall_materials, many=True)
        return Response({"wall_materials": serializer.data})


class RecordView(APIView):
    def get(self, request):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response({"records": serializer.data})
