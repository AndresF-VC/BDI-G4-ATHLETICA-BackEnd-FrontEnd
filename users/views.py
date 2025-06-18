"""
Este módulo define las vistas de registro y autenticación de usuarios:
- CreateUserView: proporciona un endpoint para crear nuevos usuarios (registro) usando UserSerializer.
- MyTokenObtainPairView: extiende el endpoint de obtención de tokens JWT para incluir campos personalizados en la respuesta.
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