// src/api/auth.js

import api from './axiosConfig'; // <-- Usa nuestra instancia

const AUTH_URL = '/auth/'; // Ya no necesitamos la URL completa

export const login = async (username, password) => {
  const response = await api.post(AUTH_URL + 'token/', { // Usa api, no axios
    username,
    password,
  });
  if (response.data.access) {
    localStorage.setItem('accessToken', response.data.access);
    localStorage.setItem('refreshToken', response.data.refresh);
  }
  return response.data;
};

export const register = async (userData) => {
  const response = await api.post(AUTH_URL + 'register/', userData); // Usa api
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};