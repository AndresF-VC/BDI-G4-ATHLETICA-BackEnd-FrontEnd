// src/context/AuthContext.jsx

import React, { createContext, useState, useContext, useEffect } from 'react';
import { login, logout } from '../api/auth'; // Importamos las funciones de la API

// 1. Creamos el Contexto
const AuthContext = createContext();

// Hook personalizado para usar el contexto más fácilmente
export const useAuth = () => {
  return useContext(AuthContext);
};

// 2. Creamos el Proveedor del Contexto
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null); // Opcional: para guardar datos del usuario

  // Efecto para verificar si ya hay un token al cargar la app
  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      setIsAuthenticated(true);
      // Aquí podríamos decodificar el token para obtener datos del usuario
    }
  }, []);

  // Función de login que actualiza el estado global
  const loginContext = async (username, password) => {
    const data = await login(username, password);
    setIsAuthenticated(true);
    // Podríamos guardar el usuario aquí si la API lo devuelve
    // setUser(data.user); 
    return data;
  };

  // Función de logout que actualiza el estado global
  const logoutContext = () => {
    logout(); // Llama a la función que borra los tokens
    setIsAuthenticated(false);
    setUser(null);
  };

  const value = {
    isAuthenticated,
    user,
    loginContext,
    logoutContext,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};