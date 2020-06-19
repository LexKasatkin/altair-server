from django.urls import path
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from realty.views import DistrictView, CityView, RealtyTypeView, FlatTypeView, DeveloperView, WallMaterialView, \
    FlatListView, StreetView, ResidentialComplexView, ImageView, AlbumView, FlatViewSet

app_name = "realty"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('cities/', CityView.as_view()),
    path('flat-types/', FlatTypeView.as_view()),
    path('developers/', DeveloperView.as_view()),
    path('wall-materials/', WallMaterialView.as_view()),
    path('flats/', FlatListView.as_view()),
    path('districts/', DistrictView.as_view()),
    path('realty-types/', RealtyTypeView.as_view()),
    path('images/', ImageView.as_view()),
    path('residential-complexes/', ResidentialComplexView.as_view()),
    path('streets/', StreetView.as_view()),
    path('albums/', AlbumView.as_view()),
    path('flats/<int:pk>', FlatViewSet.as_view({'get': 'retrieve'})),
]