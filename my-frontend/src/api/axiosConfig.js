// src/api/axiosConfig.js

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api' // URL base de tu API
});


// Interceptor para añadir el token a cada petición
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;