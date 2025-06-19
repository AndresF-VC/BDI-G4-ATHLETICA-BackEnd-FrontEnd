"""
This module defines the REST API endpoints for the main sports-domain models. It includes:
AthleteViewSet: full CRUD management of athletes with dynamic filters and permission controls.
Read-only ViewSets for Nationalities, Categories, and Clubs, which expose ordered listings.
Each class uses its own serializer and applies permissions according to the action being performed.
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
    Athlete ViewSet: supports listing, creating, updating, and deleting athlete records.
* Uses `AthleteSerializer` for lists and `AthleteDetailSerializer` for detailed operations.
* Filters its queryset based on the user’s role (admin, coach, or other).
* Applies dynamic permissions: only admins or coaches may modify; authenticated users may view details; anyone may list.
* Passes the request context into the serializer and logs initial training sessions when a new athlete is created.

    """
    serializer_class = AthleteSerializer

    def get_queryset(self):
        """
       Returns the set of athletes visible according to the user’s role:

    * Unauthenticated users: full list with no special filters.
    * Admin: access to all athletes.
    * Coach: only those athletes linked to that coach’s training sessions.
    * Other roles: full list by default.

    Uses `select_related` to optimize related-object queries.

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
        Define permissions based on the action:

        * create, update, partial\_update, destroy: IsAdminOrCoach
        * retrieve: IsAuthenticatedUser
        * list: open permissions (AllowAny)

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
        Adds the request object to the serializer context for metadata access.
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        """
        When creating an athlete (POST), save the record and, if the user is a coach,
        generate an entry in Trainings to link the new athlete with that coach.

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
        # Selects the serializer based on the action:
        # - list: AthleteSerializer (basic fields)
        # - retrieve/create/update: AthleteDetailSerializer (all fields)

        """
        if self.action == 'list':
            return AthleteSerializer
        return AthleteDetailSerializer


# The following read-only ViewSets expose listings ordered by name,
# accessible to any user:
class NationalityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lists all nationalities ordered alphabetically.
    """
    queryset = Nationalities.objects.all().order_by('name')
    serializer_class = NationalitySerializer
    permission_classes = [permissions.AllowAny]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lists all competition categories ordered alphabetically.

    """
    queryset = Categories.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lists all sports clubs ordered alphabetically.
    """
    queryset = Clubs.objects.all().order_by('name')
    serializer_class = ClubSerializer
    permission_classes = [permissions.AllowAny]