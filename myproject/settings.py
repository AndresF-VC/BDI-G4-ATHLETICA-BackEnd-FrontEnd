import os
from pathlib import Path

import environ

# ─── 1. Entorno / Variables de entorno ───────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # Valores por defecto
    DEBUG=(bool, False),
)

# Lee el .env que creaste en la raíz
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG     = env('DEBUG')

ALLOWED_HOSTS = []


# ─── 2. Aplicaciones y middleware ──────────────────────────────────────────

INSTALLED_APPS = [
    # Apps Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'corsheaders',

    # Tu app
    'core',
    'users',
]

MIDDLEWARE = [
    # CORS debe ir lo más arriba posible
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Orígenes permitidos para CORS (Vite dev server)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

ROOT_URLCONF = 'myproject.urls'


# ─── 3. Plantillas ─────────────────────────────────────────────────────────

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ─── 4. WSGI ────────────────────────────────────────────────────────────────

WSGI_APPLICATION = 'myproject.wsgi.application'


# ─── 5. Base de datos ──────────────────────────────────────────────────────

DATABASES = {
    'default': {
        'ENGINE':   env('DB_ENGINE'),
        'HOST':     env('DB_HOST'),
        'PORT':     env('DB_PORT'),
        'NAME':     env('DB_NAME'),
        'USER':     env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'OPTIONS': {
            'options': '-c search_path=olympus,public'
        },
    }
}


# ─── 6. Validación de contraseñas ─────────────────────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ─── 7. Internacionalización ───────────────────────────────────────────────

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True


# ─── 8. Archivos estáticos ─────────────────────────────────────────────────

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ─── 9. Django REST Framework (opcional) ─────────────────────────────────

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


# ─── 10. Otros ─────────────────────────────────────────────────────────────

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'

SIMPLE_JWT = {
    'USER_ID_FIELD': 'id',      
    'USER_ID_CLAIM': 'user_id', 
}