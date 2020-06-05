from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.models import City, District, Flat, Developer


class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        return Response({"cities": cities})


class DistrictView(APIView):
    def get(self, request):
        districts = District.objects.all()
        return Response({"districts": districts})


class FlatView(APIView):
    def get(self, request):
        flats = Flat.objects.all()
        return Response({"flats": flats})


class DeveloperView(APIView):
    def get(self, request):
        developers = Developer.objects.all()
        return Response({"developers": developers})


class SubjectOfLawView(APIView):
    def get(self, request):
        subjectsOfLaw = City.objects.all()
        return Response({"subjectsOfLaw": subjectsOfLaw})


class WallMaterialView(APIView):
    def get(self, request):
        wall_materials = City.objects.all()
        return Response({"wall_materials": wall_materials})


class ArticleView(APIView):
    def get(self, request):
        cities = City.objects.all()
        return Response({"cities": cities})
