import axios from 'axios'

export const api = axios.create({
  baseURL: '/api/',
  headers: { 'Content-Type': 'application/json' },
})

export const fetchAthletes = () => api.get('athletes/')
export const createAthlete = data => api.post('athletes/', data)
export const updateAthlete = (id, data) => api.put(`athletes/${id}/`, data)
export const deleteAthlete = id => api.delete(`athletes/${id}/`)
