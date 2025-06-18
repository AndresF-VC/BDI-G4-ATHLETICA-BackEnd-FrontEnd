// src/api/axiosConfig.js

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api' // URL base de tu API
});

// --- ¡LA MAGIA OCURRE AQUÍ! ---
// Interceptor para añadir el token a cada petición
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Si el error es 401 (Unauthorized)...
    if (error.response && error.response.status === 401) {
      // Borramos los tokens y recargamos la página para forzar el login.
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      window.location.href = '/login'; 
    }
    return Promise.reject(error);
  }
);

export default api;