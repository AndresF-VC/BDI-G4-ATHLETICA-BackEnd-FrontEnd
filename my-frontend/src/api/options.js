//This module provides helper functions to retrieve reference data via the configured Axios `api` instance:

//getNationalities: sends a GET request to `/nationalities/` to fetch all nationalities.
//getCategories: sends a GET request to `/categories/` to fetch all competition categories.
//getClubs: sends a GET request to `/clubs/` to fetch all sports clubs.

//Each function returns the promise from the `api.get` call for further handling (e.g., then/catch).

import api from './axiosConfig';

export const getNationalities = () => api.get('/nationalities/');
export const getCategories = () => api.get('/categories/');
export const getClubs = () => api.get('/clubs/');