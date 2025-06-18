# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
# --- LÍNEA MODIFICADA ---
# Quitamos ParticipationViewSet porque ya no lo usamos en este archivo
from .api import AthleteViewSet
from .api import AthleteViewSet, NationalityViewSet, CategoryViewSet, ClubViewSet

router = DefaultRouter()
router.register(r'athletes', AthleteViewSet, basename='athlete')
# --- NUEVAS RUTAS PARA LOS SELECTS ---
router.register(r'nationalities', NationalityViewSet, basename='nationality')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'clubs', ClubViewSet, basename='club')

urlpatterns = router.urls