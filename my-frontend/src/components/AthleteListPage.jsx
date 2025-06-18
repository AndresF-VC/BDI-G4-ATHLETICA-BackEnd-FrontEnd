// src/components/AthleteListPage.jsx

import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getAthletes, deleteAthlete } from '../api/athletes';
import { useAuth } from '../context/AuthContext';
import { useUserRole } from '../hooks/useUserRole'; 

export default function AthleteListPage() {
  const [athletes, setAthletes] = useState([]);
  const [loading, setLoading] = useState(true); // Inicia en true
  const [error, setError] = useState(null); // Estado para manejar errores
  const { isAuthenticated } = useAuth();
  const userRole = useUserRole();
  const navigate = useNavigate();

  const fetchAthletes = async () => {
    // Ponemos loading en true al empezar a buscar de nuevo (útil para refrescar)
    setLoading(true); 
    setError(null);
    try {
      const response = await getAthletes();
      setAthletes(response.data);
    } catch (err) {
      console.error("Error al obtener los atletas:", err);
      setError("No se pudo cargar la lista de atletas.");
    } finally {
      // --- ESTA ES LA LÍNEA MÁS IMPORTANTE ---
      // Se ejecuta siempre, tanto si hay éxito como si hay error.
      setLoading(false);
    }
  };

  // El useEffect solo se ejecuta una vez, cuando el componente se monta.
  useEffect(() => {
    fetchAthletes();
  }, []); // El array de dependencias vacío asegura que se ejecute solo una vez.

  const handleDelete = async (id) => {
    if (window.confirm('¿Estás seguro de que quieres borrar este atleta?')) {
      try {
        await deleteAthlete(id);
        // Volvemos a llamar a fetchAthletes para refrescar la lista
        fetchAthletes(); 
      } catch (err) {
        console.error("Error al borrar el atleta:", err);
        alert('No se pudo borrar el atleta. Es posible que no tengas los permisos necesarios.');
      }
    }
  };
  
  const canPerformActions = isAuthenticated && (userRole === 'admin' || userRole === 'coach');

  // --- LÓGICA DE RENDERIZADO MEJORADA ---

  // Primero, manejamos el estado de carga
  if (loading) {
    return <div style={{ padding: '150px 20px', textAlign: 'center' }}>Cargando atletas...</div>;
  }

  // Luego, manejamos el estado de error
  if (error) {
    return <div style={{ padding: '150px 20px', textAlign: 'center', color: 'red' }}>{error}</div>;
  }

  // Finalmente, renderizamos la tabla
  return (
    <div style={{ padding: '100px 20px', maxWidth: '1200px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>{userRole === 'coach' ? 'Mis Atletas' : 'Lista de Atletas'}</h1>
        {canPerformActions && (
          <button onClick={() => navigate('/athletes/new')} style={{ padding: '10px 20px' }}>
            Crear Nuevo Atleta
          </button>
        )}
      </div>
      
      <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={{ padding: '12px', border: '1px solid #ddd', textAlign: 'left' }}>Nombre</th>
            <th style={{ padding: '12px', border: '1px solid #ddd', textAlign: 'left' }}>Nacionalidad</th>
            <th style={{ padding: '12px', border: '1px solid #ddd', textAlign: 'left' }}>Categoría</th>
            {canPerformActions && <th style={{ padding: '12px', border: '1px solid #ddd', textAlign: 'left' }}>Acciones</th>}
          </tr>
        </thead>
        <tbody>
          {athletes.length === 0 ? (
            <tr>
              <td colSpan={canPerformActions ? 4 : 3} style={{ padding: '20px', textAlign: 'center' }}>
                No se encontraron atletas.
              </td>
            </tr>
          ) : (
            athletes.map(athlete => (
              <tr key={athlete.athlete_id}>
                <td style={{ padding: '12px', border: '1px solid #ddd' }}>
                  <Link to={`/athlete/${athlete.athlete_id}`}>{athlete.name}</Link>
                </td>
                <td style={{ padding: '12px', border: '1px solid #ddd' }}>{athlete.nationality_name}</td>
                <td style={{ padding: '12px', border: '1px solid #ddd' }}>{athlete.category_name}</td>
                {canPerformActions && (
                  <td style={{ padding: '12px', border: '1px solid #ddd' }}>
                    <button onClick={() => navigate(`/athletes/edit/${athlete.athlete_id}`)}>Editar</button>
                    <button onClick={() => handleDelete(athlete.athlete_id)} style={{ marginLeft: '10px', backgroundColor: '#dc3545', color: 'white', border: 'none' }}>Borrar</button>
                  </td>
                )}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}