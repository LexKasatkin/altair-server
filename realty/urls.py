from django.urls import path

from realty.views import DistrictView, CityView, FlatTypeView, DeveloperView, WallMaterialView, FlatView

app_name = "realty"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('cities/', CityView.as_view()),
    path('flat-types/', FlatTypeView.as_view()),
    path('developers/', DeveloperView.as_view()),
    path('wall-materials/', WallMaterialView.as_view()),
    path('flats/', FlatView.as_view()),
    path('districts/', DistrictView.as_view()),

]
