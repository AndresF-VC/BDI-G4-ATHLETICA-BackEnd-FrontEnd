"""
Este módulo define los endpoints de la API REST para los modelos principales del dominio deportivo.
Se incluyen:
- AthleteViewSet: gestión completa (CRUD) de deportistas con permisos y filtros dinámicos.
- ViewSets de solo lectura para Nationalities, Categories y Clubs, que exponen listados ordenados.

Las clases usan serializers específicos y asignan permisos según la acción solicitada.
"""

from rest_framework import viewsets, permissions  # Importa clases base para viewsets y permisos
from .models import Athletes, Trainings, Nationalities, Categories, Clubs
from .serializers import (
    AthleteSerializer,
    AthleteDetailSerializer,
    NationalitySerializer,
    CategorySerializer,
    ClubSerializer,
)
from .permissions import IsAdminOrCoach, IsAuthenticatedUser


class AthleteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para deportistas (Athletes): permite listar, crear, actualizar y eliminar registros.
    - Usa AthleteSerializer para listados y AthleteDetailSerializer para operaciones detalladas.
    - Filtra el queryset según el rol del usuario (admin, coach u otros).
    - Asigna permisos dinámicos: solo admin o coach pueden modificar; usuarios autenticados pueden ver detalles; cualquiera puede listar.
    - Añade contexto de request al serializer y registra entrenamientos iniciales al crear un atleta.
    """
    serializer_class = AthleteSerializer

    def get_queryset(self):
        """
        Devuelve el conjunto de atletas visibles según el rol del usuario:
        - No autenticados: listado completo sin filtros especiales.
        - Admin: acceso a todos los atletas.
        - Coach: solo atletas vinculados a entrenamientos de ese coach.
        - Otros roles: listado completo por defecto.
        Se usa select_related para optimizar consultas de relaciones.
        """
        user = self.request.user

        if not user.is_authenticated:
            return Athletes.objects.all().select_related('nationality', 'category', 'club')

        if user.role == 'admin':
            return Athletes.objects.all().select_related('nationality', 'category', 'club')

        if user.role == 'coach' and hasattr(user, 'coach'):
            return (
                Athletes.objects
                .filter(trainings__coach=user.coach)
                .distinct()
                .select_related('nationality', 'category', 'club')
            )

        return Athletes.objects.all().select_related('nationality', 'category', 'club')
    
    def get_permissions(self):
        """
        Define permisos según la acción:
        - create, update, partial_update, destroy: IsAdminOrCoach
        - retrieve: IsAuthenticatedUser
        - list: permisos abiertos (AllowAny)
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrCoach]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticatedUser]
        else:
            permission_classes = [permissions.AllowAny]

        return [perm() for perm in permission_classes]

    def get_serializer_context(self):
        """
        Añade el objeto request al contexto del serializer para acceso a metadata.
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        """
        Al crear un atleta (POST), guarda el registro y, si el usuario es coach,
        genera una entrada en Trainings para vincular al nuevo atleta con ese coach.
        """
        athlete = serializer.save()
        user = self.request.user
        if user.role == 'coach' and hasattr(user, 'coach'):
            Trainings.objects.create(
                athlete=athlete,
                coach=user.coach,
                training_type='Initial Assessment',
            )

    def get_serializer_class(self):
        """
        Selecciona el serializer según la acción:
        - list: AthleteSerializer (datos básicos)
        - retrieve/create/update: AthleteDetailSerializer (todos los campos)
        """
        if self.action == 'list':
            return AthleteSerializer
        return AthleteDetailSerializer


# Los siguientes ViewSets de solo lectura exponen listados ordenados por nombre,
# accesibles para cualquier usuario:
class NationalityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lista todas las nacionalidades ordenadas alfabéticamente.
    """
    queryset = Nationalities.objects.all().order_by('name')
    serializer_class = NationalitySerializer
    permission_classes = [permissions.AllowAny]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lista todas las categorías de competencia ordenadas alfabéticamente.
    """
    queryset = Categories.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lista todos los clubes deportivos ordenados alfabéticamente.
    """
    queryset = Clubs.objects.all().order_by('name')
    serializer_class = ClubSerializer
    permission_classes = [permissions.AllowAny]
