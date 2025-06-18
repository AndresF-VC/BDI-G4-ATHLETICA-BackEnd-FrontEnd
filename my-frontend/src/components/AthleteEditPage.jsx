// src/components/AthleteEditPage.jsx

import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import AthleteForm from './AthleteForm';
import { getAthleteDetail, updateAthlete } from '../api/athletes';

export default function AthleteEditPage() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [initialAthleteData, setInitialAthleteData] = useState(null);

  useEffect(() => {
    // Cuando el componente se monta, busca los datos del atleta
    getAthleteDetail(id)
      .then(res => {
        // Guardamos los datos completos que nos devuelve el AthleteDetailSerializer
        setInitialAthleteData(res.data);
      })
      .catch(err => {
        console.error("Error al cargar datos para editar:", err);
        // Opcional: redirigir si no se encuentra el atleta
        navigate('/athletes'); 
      });
  }, [id, navigate]);

  const handleUpdate = async (formData) => {
    // Al enviar el formulario, creamos el objeto que espera el backend.
    // Nuestro serializer de escritura espera 'name', 'birth_date', etc.,
    // y los IDs de 'nationality', 'category' y 'club'.
    const dataToSubmit = {
      name: formData.name,
      birth_date: formData.birth_date,
      gender: formData.gender,
      nationality: formData.nationality,
      category: formData.category,
      club: formData.club || null, // Envía null si el club está vacío
    };
    await updateAthlete(id, dataToSubmit);
    alert('¡Atleta actualizado con éxito!');
    navigate('/athletes');
  };
  
  // Mientras no tengamos los datos, mostramos un mensaje de carga.
  if (!initialAthleteData) {
    return <p style={{padding: '150px 20px'}}>Cargando datos del atleta...</p>;
  }

  // Cuando ya tenemos los datos, renderizamos el formulario y se los pasamos.
  return (
    <AthleteForm 
      onSubmit={handleUpdate} 
      initialData={initialAthleteData}
      isEditing={true} 
    />
  );
}