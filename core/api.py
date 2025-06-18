# core/api.py

from rest_framework import viewsets, permissions # <-- 1. IMPORTA 'permissions'
from .models import Athletes, Trainings # Importamos Trainings para el filtro
from .serializers import AthleteSerializer
from .permissions import IsAdminOrCoach, IsAuthenticatedUser
from .models import Nationalities, Categories, Clubs
from .serializers import NationalitySerializer, CategorySerializer, ClubSerializer
from .serializers import AthleteSerializer, AthleteDetailSerializer 

class AthleteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Atletas con permisos y queryset dinámicos.
    """
    serializer_class = AthleteSerializer
    # --- 2. ELIMINAMOS permission_classes DE AQUÍ ---
    # Porque ya lo manejamos con el método get_permissions

    def get_queryset(self):
        """
        Filtra los atletas visibles según el rol del usuario.
        """
        user = self.request.user

        if not user.is_authenticated:
            # Usuarios no logueados no ven atletas en la lista principal.
            # O podrías devolver Athletes.objects.none() si no quieres que vean nada.
            return Athletes.objects.all().select_related('nationality', 'category', 'club')

        if user.role == 'admin':
            return Athletes.objects.all().select_related('nationality', 'category', 'club')

        if user.role == 'coach' and hasattr(user, 'coach'):
            # Filtra por atletas que tienen un entrenamiento con el coach logueado
            return Athletes.objects.filter(trainings__coach=user.coach).distinct().select_related('nationality', 'category', 'club')

        # Para otros roles (como 'athlete'), devolvemos todos por ahora
        return Athletes.objects.all().select_related('nationality', 'category', 'club')

    def get_permissions(self):
        """
        Asigna permisos dinámicamente según la acción.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrCoach]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticatedUser]
        else: # 'list'
            permission_classes = [permissions.AllowAny] # <-- 3. Usamos permissions.AllowAny

        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        """
        Pasa el request al contexto del serializer.
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    
    def perform_create(self, serializer):
        """
        Este método se ejecuta al crear un nuevo atleta (petición POST).
        """
        # Primero, guardamos el atleta con los datos del formulario.
        athlete = serializer.save()

        # Obtenemos el usuario que está haciendo la petición.
        user = self.request.user

        # Si el usuario es un coach y tiene un perfil de coach asociado...
        if user.role == 'coach' and hasattr(user, 'coach'):
            # Creamos un registro en la tabla de entrenamientos para vincular
            # al nuevo atleta con el coach que lo está creando.
            Trainings.objects.create(
                athlete=athlete,
                coach=user.coach,
                # Podemos añadir valores por defecto o dejar los otros campos en null
                training_type='Initial Assessment' 
            )
        
    def get_serializer_class(self):
        """
        Devuelve la clase de serializer a usar dependiendo de la acción.
        """
        # Para la vista de lista, usamos el serializer simple.
        if self.action == 'list':
            return AthleteSerializer
        
        # Para cualquier otra acción (retrieve, create, update), 
        # usamos el serializer de detalle que tiene todos los campos.
        return AthleteDetailSerializer

class NationalityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de solo lectura para obtener la lista de nacionalidades.
    """
    queryset = Nationalities.objects.all().order_by('name')
    serializer_class = NationalitySerializer
    permission_classes = [permissions.AllowAny] # Cualquiera puede ver la lista

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de solo lectura para obtener la lista de categorías.
    """
    queryset = Categories.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de solo lectura para obtener la lista de clubes.
    """
    queryset = Clubs.objects.all().order_by('name')
    serializer_class = ClubSerializer
    permission_classes = [permissions.AllowAny]