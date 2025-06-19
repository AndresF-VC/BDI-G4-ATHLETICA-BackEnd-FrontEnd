"""
Configures the Django admin for the CustomUser model, extending the default UserAdmin to:

* Include the custom fields `role`, `athlete`, and `coach` in the creation and editing forms.
* Display the `role` field alongside the basic user information in the user list.
"""
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from core.serializers import UserSerializer, MyTokenObtainPairSerializer 


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer