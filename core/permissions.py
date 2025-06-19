"""
Custom permissions for the Core API:

* IsAdminOrCoach: authorizes administrators and coaches based on their assigned athletes.
* IsReadOnly: allows only read-only methods.
* IsAuthenticatedUser: restricts all operations to authenticated users.

"""

from rest_framework.permissions import BasePermission
from .models import Trainings

class IsAdminOrCoach(BasePermission):
    """
    Allows full access to users with the ‘admin’ role 
    and grants coaches access only to their assigned athletes.
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
    Allows only read-only methods.

    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsAuthenticatedUser(BasePermission):
    """
    Restricts all operations to authenticated users.

    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
