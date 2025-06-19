/**
 * API helper module: configures Axios and provides CRUD methods for athletes.
 *
 * Exports:
 * - api: Axios instance with baseURL '/api/' and JSON content headers.
 * - fetchAthletes(): GET '/athletes/' to retrieve all athletes.
 * - createAthlete(data): POST '/athletes/' to create a new athlete.
 * - updateAthlete(id, data): PUT '/athletes/{id}/' to update an athlete by ID.
 * - deleteAthlete(id): DELETE '/athletes/{id}/' to remove an athlete by ID.
 */

import axios from 'axios'

export const api = axios.create({
  baseURL: '/api/',
  headers: { 'Content-Type': 'application/json' },
})

export const fetchAthletes = () => api.get('athletes/')
export const createAthlete = data => api.post('athletes/', data)
export const updateAthlete = (id, data) => api.put(`athletes/${id}/`, data)
export const deleteAthlete = id => api.delete(`athletes/${id}/`)
