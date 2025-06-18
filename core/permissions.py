"""
Permisos personalizados para la API de Core:
- IsAdminOrCoach: autoriza a administradores y entrenadores según sus atletas asignados.
- IsReadOnly: permite únicamente métodos de solo lectura.
- IsAuthenticatedUser: restringe todas las operaciones a usuarios autenticados.
"""

from rest_framework.permissions import BasePermission
from .models import Trainings

class IsAdminOrCoach(BasePermission):
    """
    Permite acceso total a usuarios con rol 'admin' y a entrenadores
    solo sobre sus atletas asignados.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in ['admin', 'coach']

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if request.user.role == 'coach':
            return Trainings.objects.filter(
                athlete=obj,
                coach=request.user.coach
            ).exists()
        return False

class IsReadOnly(BasePermission):
    """
    Permite únicamente métodos de solo lectura.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsAuthenticatedUser(BasePermission):
    """
    Restringe todas las operaciones a usuarios autenticados.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
