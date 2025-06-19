//This module configures the Axios instance for API requests:

//Creates an Axios instance with `baseURL` set to `http://localhost:8000/api`.
//Adds a request interceptor that retrieves the `accessToken` from `localStorage` and, if present, sets the `Authorization` header to `Bearer <token>`.
//Handles request errors by rejecting the promise with the error.
//Exports the configured `api` instance for use across the application.


import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api' 
});


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