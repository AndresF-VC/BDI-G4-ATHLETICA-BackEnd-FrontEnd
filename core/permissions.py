# core/permissions.py

from rest_framework.permissions import BasePermission
# --- 1. IMPORTA EL MODELO NECESARIO ---
from .models import Trainings

class IsAdminOrCoach(BasePermission):
    """
    Permiso personalizado que permite:
    - Acceso total a los usuarios con rol 'admin'.
    - Acceso de edición/borrado a los 'coach' SOLO sobre sus atletas asignados.
    """

    def has_permission(self, request, view):
        """
        Verifica si el usuario tiene permiso para la acción a nivel general.
        """
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in ['admin', 'coach']

    def has_object_permission(self, request, view, obj):
        """
        Verifica si el usuario tiene permiso sobre un objeto específico (un atleta).
        """
        # Los administradores tienen permiso sobre cualquier objeto.
        if request.user.role == 'admin':
            return True

        # Si el usuario es un coach, verificamos la relación.
        if request.user.role == 'coach':
            # Ahora Python sabe qué es 'Trainings' gracias a la importación.
            return Trainings.objects.filter(athlete=obj, coach=request.user.coach).exists()
            
        return False

# --- OTRAS CLASES DE PERMISOS (SIN CAMBIOS) ---

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        # ...
        return request.method in permissions.SAFE_METHODS

class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        # ...
        return request.user and request.user.is_authenticated