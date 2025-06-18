// src/AthleteDetail.jsx

import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Carousel } from 'react-responsive-carousel';
// --- 1. IMPORTAMOS NUESTRA FUNCIÓN DE API ---
import { getAthleteDetail } from './api/athletes'; 
import './AthleteDetail.css';

export default function AthleteDetail() {
  const { id } = useParams();
  const [athlete, setAthlete] = useState(null);
  // Ya no necesitamos un estado para participations, vendrá dentro del atleta
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Fondos (se mantiene igual)
  const bgImages = [
    '/images/athlete1.jpg',
    '/images/athlete2.jpg',
    '/images/athlete3.jpg',
  ];

  useEffect(() => {
    // Si no hay ID en la URL, no hacemos nada.
    if (!id) return;

    const fetchAthlete = async () => {
      try {
        // --- 2. USAMOS NUESTRA NUEVA FUNCIÓN ---
        // Hacemos una única llamada que ya incluye el token de autenticación
        const response = await getAthleteDetail(id);
        setAthlete(response.data);
      } catch (err) {
        console.error("Error al obtener el detalle del atleta:", err);
        setError("No se pudo cargar la información. Es posible que necesites iniciar sesión para ver los detalles completos de este atleta.");
      } finally {
        setLoading(false);
      }
    };

    fetchAthlete();
  }, [id]);

  // --- 3. MEJORAMOS LOS ESTADOS DE CARGA Y ERROR ---
  if (loading) {
    return <p className="detail-loading">Cargando...</p>;
  }

  if (error) {
    // Mostramos un mensaje claro si hay un error (como el 401 Unauthorized)
    return <p className="detail-loading" style={{ color: 'red' }}>{error}</p>;
  }

  if (!athlete) {
    // Si no hay error pero tampoco atleta, mostramos que no se encontró
    return <p className="detail-loading">Atleta no encontrado.</p>;
  }
  
  // Extraemos las participaciones del objeto atleta
  const participations = athlete.participations || [];

  return (
    <div className="detail-page">
      <Carousel
        className="detail-bg-carousel"
        autoPlay
        infiniteLoop
        showThumbs={false}
        showStatus={false}
        interval={4000}
        transitionTime={800}
      >
        {bgImages.map((src, i) => (
          <div key={i} className="detail-bg-slide">
            <img src={src} alt={`fondo-${i}`} />
          </div>
        ))}
      </Carousel>

      <div className="detail-content">
        <Link to="/athletes" className="detail-back">← Volver a la lista</Link>
        <h2 className="detail-title">{athlete.name}</h2>

        {/* --- 4. USAMOS LOS NOMBRES CORRECTOS DEL SERIALIZER --- */}
        <p><strong>Fecha de nacimiento:</strong> {athlete.birth_date}</p>
        <p><strong>Género:</strong> {athlete.gender}</p>
        <p><strong>Nacionalidad:</strong> {athlete.nationality_name}</p>
        <p><strong>Categoría:</strong> {athlete.category_name}</p>
        <p><strong>Club:</strong> {athlete.club_name || 'No especificado'}</p>

        <div className="participations-container">
          <h3>Participaciones</h3>
          {participations.length === 0 ? (
            <p>No hay participaciones registradas.</p>
          ) : (
            <ul className="participations-list">
              {participations.map(p => (
                <li key={p.participation_id}>
                  <strong>{p.event_name} ({p.discipline_name}):</strong> posición {p.position}, tiempo {p.result}
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
