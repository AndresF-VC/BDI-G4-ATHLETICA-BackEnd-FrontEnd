
//This module provides helper functions for interacting with the Athletes API via Axios:

//getAthletes: fetches the full list of athletes.

//getAthleteDetail: retrieves detailed information for a single athlete by ID.

//createAthlete: submits data to create a new athlete record.

//updateAthlete: sends updated data to modify an existing athlete by ID.

//deleteAthlete: removes an athlete record by ID.

import api from './axiosConfig'; 

const ATHLETES_URL = '/athletes/';



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