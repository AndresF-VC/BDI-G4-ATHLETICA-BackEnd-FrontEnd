/**
 * ProfilePage component: displays the current user's profile information.
 *
 * Behavior:
 * - Retrieves the authenticated user from AuthContext.
 * - Renders a heading and welcome message.
 * - Shows username and email if user data is available.
 */
import React from 'react';
import { useAuth } from '../context/AuthContext';

export default function ProfilePage() {
  const { user } = useAuth();

  return (
    <div style={{ padding: '150px 20px' }}>
      <h1>Mi Perfil</h1>
      <p>¡Bienvenido! Esta es tu página de perfil.</p>
      {/* Later, we'll display the user's information here */}
      {user && (
        <div>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      )}
    </div>
  );
}