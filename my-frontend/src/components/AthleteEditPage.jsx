/**
 * AthleteEditPage: loads athlete data by ID, renders AthleteForm for editing,
 * and handles update submission.
 */
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import AthleteForm from './AthleteForm';
import { getAthleteDetail, updateAthlete } from '../api/athletes';

export default function AthleteEditPage() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [initialAthleteData, setInitialAthleteData] = useState(null);

  useEffect(() => {
    getAthleteDetail(id)
      .then(res => {
        setInitialAthleteData(res.data);
      })
      .catch(err => {
        console.error("Error al cargar datos para editar:", err);
        navigate('/athletes'); 
      });
  }, [id, navigate]);

  const handleUpdate = async (formData) => {
    const dataToSubmit = {
      name: formData.name,
      birth_date: formData.birth_date,
      gender: formData.gender,
      nationality: formData.nationality,
      category: formData.category,
      club: formData.club || null, 
    };
    await updateAthlete(id, dataToSubmit);
    alert('¡Atleta actualizado con éxito!');
    navigate('/athletes');
  };
  
  if (!initialAthleteData) {
    return <p style={{padding: '150px 20px'}}>Cargando datos del atleta...</p>;
  }

  return (
    <AthleteForm 
      onSubmit={handleUpdate} 
      initialData={initialAthleteData}
      isEditing={true} 
    />
  );
}