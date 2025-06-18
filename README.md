# 🏃‍♂️ Athletica: Sistema de Gestión Deportiva Integral

**Desarrolladores**: Cesar Posso y Diego Fernandez  
**Stack Tecnológico**: Django (Backend) + React con Vite (Frontend)  
**Base de Datos**: PostgreSQL

---

## 📝 Descripción General

**Athletica** es una aplicación web full-stack diseñada para la gestión y seguimiento de atletas, entrenadores y eventos deportivos. La plataforma ofrece un backend robusto construido con **Django** y **Django REST Framework** para manejar la lógica de negocio y una API segura, junto con un frontend moderno y reactivo desarrollado con **React** y **Vite** para una experiencia de usuario fluida e intuitiva.

El sistema permite un control de acceso basado en roles, asegurando que atletas, entrenadores y administradores tengan acceso a las funcionalidades y datos que les corresponden.

---

## ✨ Características Principales

-   **Gestión de Atletas (CRUD)**: Funcionalidad completa para crear, leer, actualizar y eliminar perfiles de atletas, incluyendo datos personales, club y categoría.
-   **Sistema de Autenticación Completo**: Registro de nuevos usuarios, inicio de sesión seguro con tokens **JWT**, y cierre de sesión.
-   **Permisos Basados en Roles**:
    -   **Invitados**: Pueden ver listas públicas (como la de atletas).
    -   **Atletas**: Pueden ver su propio perfil y estadísticas detalladas.
    -   **Entrenadores**: Pueden gestionar (crear, editar, borrar) únicamente a los atletas que tienen asignados.
    -   **Administradores**: Tienen control total sobre todos los datos a través de la API y el panel de administración de Django.
-   **Interfaz de Usuario Moderna**: Desarrollada con React y Vite para una carga rápida y una navegación ágil sin recargar la página.
-   **Poblado de Datos Automatizado**: Incluye un script de gestión para poblar la base de datos con datos de prueba realistas.

---

## 🛠️ Tecnologías Utilizadas

### Backend
-   **Framework**: Django 5.x
-   **API**: Django REST Framework
-   **Autenticación**: djangorestframework-simplejwt (Tokens JWT)
-   **Base de Datos**: PostgreSQL
-   **Variables de Entorno**: django-environ

### Frontend
-   **Librería**: React 18.x
-   **Bundler**: Vite
-   **Routing**: React Router DOM
-   **Peticiones HTTP**: Axios
-   **Gestión de Estado**: React Context API
-   **Decodificación de Tokens**: jwt-decode

---

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto completo en tu entorno local.

### **1. Requisitos Previos**

-   Python 3.10+
-   Node.js 18.x+ y npm
-   PostgreSQL instalado y corriendo.

### **2. Configuración del Backend (Django)**

1.  **Clona el repositorio** y navega a la carpeta del proyecto.
2.  **Navega a la carpeta del backend**:
    ```bash
    cd backend_y_frontend_copia # O el nombre de tu carpeta de backend
    ```
3.  **Crea y activa un entorno virtual**:
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\Activate
    # En macOS/Linux
    source venv/bin/activate
    ```
4.  **Instala las dependencias de Python**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Configura las variables de entorno**:
    -   Crea un archivo `.env` en la raíz de la carpeta del backend.
    -   Copia el contenido de `.env.example` (si existe) o añade las siguientes variables, ajustando los valores a tu configuración de PostgreSQL:
    ```env
    DJANGO_SECRET_KEY='tu_clave_secreta_aqui'
    DEBUG=True
    DB_ENGINE=django.db.backends.postgresql
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=sportsdb
    DB_USER=sports_admin
    DB_PASSWORD=tu_contraseña_de_bd
    ```
6.  **Prepara la base de datos**:
    -   Asegúrate de que la base de datos (`sportsdb`) y el usuario (`sports_admin`) existan en PostgreSQL y que el usuario tenga permisos sobre la base de datos.
    -   Aplica las migraciones para crear las tablas:
    ```bash
    python manage.py migrate
    ```
7.  **(Opcional) Puebla la base de datos con datos de prueba**:
    ```bash
    python manage.py populate_db
    ```
8.  **Inicia el servidor del backend**:
    ```bash
    python manage.py runserver
    ```
    El backend estará corriendo en `http://localhost:8000`.

### **3. Configuración del Frontend (React)**

1.  **Abre una nueva terminal**.
2.  **Navega a la carpeta del frontend**:
    ```bash
    cd my-frontend # O el nombre de tu carpeta de frontend
    ```
3.  **Instala las dependencias de Node.js**:
    ```bash
    npm install
    ```
4.  **Inicia el servidor de desarrollo**:
    ```bash
    npm run dev
    ```
    La aplicación de React estará disponible en `http://localhost:5173`.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar el proyecto, por favor sigue estos pasos:

1.  Haz un "Fork" del repositorio.
2.  Crea una nueva rama para tu funcionalidad (`git checkout -b feature/MiNuevaFuncionalidad`).
3.  Realiza tus cambios y haz "commit" de ellos (`git commit -m 'Añade MiNuevaFuncionalidad'`).
4.  Haz "Push" a tu rama (`git push origin feature/MiNuevaFuncionalidad`).
5.  Abre un "Pull Request" para que podamos revisar tus cambios.