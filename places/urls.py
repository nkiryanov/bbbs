from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import PlacesTagList, PlacesViewSet


router = DefaultRouter()
router.register("places", PlacesViewSet, basename="places")

extra_patterns = [
    path("places/tags/", PlacesTagList.as_view(), name="places_tags"),
    path("", include(router.urls)),
]

urlpatterns = [
    path("v1/", include(extra_patterns)),
]
