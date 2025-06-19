"""
    This module configures the API routes for the Core application:

* Registers the `athletes` endpoint for athlete CRUD operations.
* Adds read-only endpoints to retrieve lists of nationalities, categories, and clubs.

"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import AthleteViewSet
from .api import AthleteViewSet, NationalityViewSet, CategoryViewSet, ClubViewSet

router = DefaultRouter()
router.register(r'athletes', AthleteViewSet, basename='athlete')
router.register(r'nationalities', NationalityViewSet, basename='nationality')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'clubs', ClubViewSet, basename='club')

urlpatterns = router.urls