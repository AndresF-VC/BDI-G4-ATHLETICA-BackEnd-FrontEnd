// src/api/athletes.js

import api from './axiosConfig'; // <-- Usa nuestra instancia

const ATHLETES_URL = '/athletes/';

// Ya no necesitamos getAuthHeaders(), el interceptor lo hace por nosotros.

export const getAthletes = () => {
  return api.get(ATHLETES_URL);
};

export const getAthleteDetail = (id) => {
  return api.get(`${ATHLETES_URL}${id}/`);
};

export const createAthlete = (athleteData) => {
  return api.post(ATHLETES_URL, athleteData);
};

export const updateAthlete = (id, athleteData) => {
  return api.put(`${ATHLETES_URL}${id}/`, athleteData);
};

export const deleteAthlete = (id) => {
  return api.delete(`${ATHLETES_URL}${id}/`);
};