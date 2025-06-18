# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from users.views import CreateUserView  # Importamos la nueva vista
from users.views import CreateUserView, MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/register/', CreateUserView.as_view(), name='register'),
    # --- LÍNEA MODIFICADA ---
    # Ahora usa nuestra vista personalizada que añade el rol al token
    path('api/auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include('core.urls')),
]