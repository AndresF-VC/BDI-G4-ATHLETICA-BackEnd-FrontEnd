/**
 * AthleteForm component: renders a form for creating or editing an athlete.
 *
 * Props:
 * - onSubmit(formData): function called when the form is submitted.
 * - initialData: object with existing athlete values when editing (default: {}).
 * - isEditing: boolean flag to indicate edit mode (default: false).
 *
 * Behavior:
 * - Loads select options (nationalities, categories, clubs) on mount via API.
 * - Initializes form fields from initialData when in edit mode.
 * - Manages loading and error states for both options fetch and form submission.
 * - Calls onSubmit with the current formData and handles API errors by displaying messages.
 */

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getNationalities, getCategories, getClubs } from '../api/options';

export default function AthleteForm({ onSubmit, initialData = {}, isEditing = false }) {
  const [formData, setFormData] = useState({
    name: '',
    birth_date: '',
    gender: 'Other',
    nationality: '',
    category: '',
    club: ''
  });

  const [options, setOptions] = useState({
    nationalities: [],
    categories: [],
    clubs: []
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchOptions = async () => {
      try {
        const [natRes, catRes, clubRes] = await Promise.all([
          getNationalities(),
          getCategories(),
          getClubs()
        ]);
        setOptions({
          nationalities: natRes.data,
          categories: catRes.data,
          clubs: clubRes.data
        });
      } catch (err) {
        setError("No se pudieron cargar las opciones del formulario.");
      } finally {
        setLoading(false);
      }
    };
    fetchOptions();
  }, []);

  useEffect(() => {
    if (isEditing && initialData.athlete_id) {
      setFormData({
        name: initialData.name || '',
        birth_date: initialData.birth_date || '',
        gender: initialData.gender || 'Other',
        nationality: initialData.nationality || '',
        category: initialData.category || '',
        club: initialData.club || ''
      });
    }
  }, [initialData, isEditing]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      await onSubmit(formData);
    } catch (err) {
      console.error('Error al guardar el atleta:', err.response?.data);
      const errorMsg = Object.values(err.response.data).flat().join(' ');
      setError(errorMsg || 'No se pudo guardar. Revisa los datos.');
    } finally {
    }
  };

  if (loading && !options.nationalities.length) {
      return <p style={{ padding: '150px 20px' }}>Cargando formulario...</p>
  }

  return (
    <form onSubmit={handleSubmit} style={{ padding: '100px 20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>{isEditing ? 'Editar Atleta' : 'Crear Nuevo Atleta'}</h1>
      
      <div style={{ marginBottom: '1rem' }}>
        <label>Nombre</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} required style={{ width: '100%', padding: '8px' }} />
      </div>
      <div style={{ marginBottom: '1rem' }}>
        <label>Fecha de Nacimiento</label>
        <input type="date" name="birth_date" value={formData.birth_date} onChange={handleChange} required style={{ width: '100%', padding: '8px' }} />
      </div>
      <div style={{ marginBottom: '1rem' }}>
        <label>Género</label>
        <select name="gender" value={formData.gender} onChange={handleChange} required style={{ width: '100%', padding: '8px' }}>
          <option value="" disabled>Selecciona un género...</option>
          <option value="Male">Masculino</option>
          <option value="Female">Femenino</option>
          <option value="Other">Otro</option>
        </select>
      </div>

      {/* --- Drop-down menus --- */}
      <div style={{ marginBottom: '1rem' }}>
        <label>Nacionalidad</label>
        <select name="nationality" value={formData.nationality} onChange={handleChange} required style={{ width: '100%', padding: '8px' }}>
          <option value="" disabled>Selecciona una nacionalidad...</option>
          {options.nationalities.map(nat => (
            <option key={nat.nationality_id} value={nat.nationality_id}>{nat.name}</option>
          ))}
        </select>
      </div>
      <div style={{ marginBottom: '1rem' }}>
        <label>Categoría</label>
        <select name="category" value={formData.category} onChange={handleChange} required style={{ width: '100%', padding: '8px' }}>
          <option value="" disabled>Selecciona una categoría...</option>
          {options.categories.map(cat => (
            <option key={cat.category_id} value={cat.category_id}>{cat.name}</option>
          ))}
        </select>
      </div>
      <div style={{ marginBottom: '1rem' }}>
        <label>Club</label>
        <select name="club" value={formData.club} onChange={handleChange} style={{ width: '100%', padding: '8px' }}>
          <option value="">Selecciona un club (opcional)...</option>
          {options.clubs.map(club => (
            <option key={club.club_id} value={club.club_id}>{club.name}</option>
          ))}
        </select>
      </div>

      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      <button type="submit" disabled={loading} style={{ padding: '10px 20px' }}>
        {loading ? 'Guardando...' : 'Guardar Atleta'}
      </button>
      <button type="button" onClick={() => navigate('/athletes')} style={{ marginLeft: '10px' }}>
        Cancelar
      </button>
    </form>
  );
}