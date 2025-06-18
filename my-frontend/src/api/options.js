// src/api/options.js
import api from './axiosConfig';

export const getNationalities = () => api.get('/nationalities/');
export const getCategories = () => api.get('/categories/');
export const getClubs = () => api.get('/clubs/');