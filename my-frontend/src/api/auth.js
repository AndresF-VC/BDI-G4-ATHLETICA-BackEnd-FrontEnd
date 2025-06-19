//This module provides helper functions for user authentication via Axios:
//login:
//  Sends `username` and `password` to `'/auth/token/'` to obtain JWT tokens.
//  On success, stores `accessToken` and `refreshToken` in `localStorage`.
// Returns the token payload (`response.data`).

//register:
//  Sends new user data to `'/auth/register/'` to create an account.
// Returns the created user data (`response.data`).

//logout:
//  Clears `accessToken` and `refreshToken` from `localStorage`.

//All functions use the base `AUTH_URL` (`'/auth/'`) and the configured `api` instance from `axiosConfig`.


import api from './axiosConfig'; 

const AUTH_URL = '/auth/'; 

export const login = async (username, password) => {
  const response = await api.post(AUTH_URL + 'token/', { 
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
  const response = await api.post(AUTH_URL + 'register/', userData); 
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};