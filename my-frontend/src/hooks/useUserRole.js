// src/hooks/useUserRole.js

import { jwtDecode } from 'jwt-decode';
import { useAuth } from '../context/AuthContext';

export const useUserRole = () => {
  const { isAuthenticated } = useAuth();
  
  // Si no está autenticado, no hay rol.
  if (!isAuthenticated) {
    return null;
  }

  const token = localStorage.getItem('accessToken');

  if (token) {
    try {
      const decodedToken = jwtDecode(token);
      // Devuelve el rol que pusimos en el token en el backend
      return decodedToken.role;
    } catch (error) {
      console.error('Token inválido:', error);
      return null;
    }
  }

  return null;
};