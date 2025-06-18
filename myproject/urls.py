"""
Este módulo define las rutas principales de la aplicación:
- Admin de Django en '/admin/'.
- Endpoints de registro de usuario y autenticación con JWT bajo '/api/auth/'.
- Inclusión de todas las rutas de la API Core en '/api/'.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from users.views import CreateUserView  
from users.views import CreateUserView, MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/register/', CreateUserView.as_view(), name='register'),
    path('api/auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include('core.urls')),
]