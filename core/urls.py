"""
    Este módulo configura las rutas de la API para la aplicación Core.
- Registra el endpoint 'athletes' para las operaciones CRUD de atletas.
- Añade endpoints de solo lectura para obtener listas de nacionalidades, categorías y clubes.
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