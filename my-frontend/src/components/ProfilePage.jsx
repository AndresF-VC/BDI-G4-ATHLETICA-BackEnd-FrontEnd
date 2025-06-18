// src/components/ProfilePage.jsx
import React from 'react';
import { useAuth } from '../context/AuthContext';

export default function ProfilePage() {
  const { user } = useAuth();

  return (
    <div style={{ padding: '150px 20px' }}>
      <h1>Mi Perfil</h1>
      <p>¡Bienvenido! Esta es tu página de perfil.</p>
      {/* Más adelante, aquí mostraremos la información del usuario */}
      {user && (
        <div>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      )}
    </div>
  );
}