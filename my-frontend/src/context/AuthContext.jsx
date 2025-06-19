/**
 * AuthContext and AuthProvider: manages global authentication state.
 *
 * Exposes:
 * - isAuthenticated: boolean flag for login status.
 * - user: optional user data object.
 * - loginContext(username, password): authenticates via API, stores tokens, updates state.
 * - logoutContext(): clears tokens and resets authentication state.
 *
 * Behavior:
 * - On app load, checks localStorage for an existing access token.
 * - Provides context to any component via useAuth() hook.
 */

import React, { createContext, useState, useContext, useEffect } from 'react';
import { login, logout } from '../api/auth'; 

const AuthContext = createContext();


export const useAuth = () => {
  return useContext(AuthContext);
};


export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null); 

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      setIsAuthenticated(true);
    }
  }, []);

  const loginContext = async (username, password) => {
    const data = await login(username, password);
    setIsAuthenticated(true);
    return data;
  };

  const logoutContext = () => {
    logout();
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