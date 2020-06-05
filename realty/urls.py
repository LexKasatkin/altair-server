from django.urls import path

from realty.views import CityView, ImageView, FlatView, DeveloperView, SubjectOfLawView, WallMaterialView, RecordView

app_name = "realty"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('cities/', CityView.as_view()),
    path('images/', ImageView.as_view()),
    path('flats/', FlatView.as_view()),
    path('developers/', DeveloperView.as_view()),
    path('subjects-of-law/', SubjectOfLawView.as_view()),
    path('wall-materials/', WallMaterialView.as_view()),
    path('records/', RecordView.as_view()),
]
