# users/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
# --- IMPORTACIONES CORREGIDAS ---
from core.serializers import UserSerializer, MyTokenObtainPairSerializer 

# --- VISTA DE REGISTRO ---
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# --- VISTA DE LOGIN CON TOKEN PERSONALIZADO ---
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer