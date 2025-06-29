/**
 * RegisterPage component: renders a registration form and handles user account creation.
 *
 * Behavior:
 * - Manages local state for username, email, password, and password confirmation.
 * - Validates that password and confirmation match before submission.
 * - Calls the register API to create a new user with role 'guest'.
 * - Displays validation and server error messages.
 * - Redirects to the login page upon successful registration.
 */

import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { register } from '../api/auth'; 

export default function RegisterPage() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState(''); 
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); 

  
    if (password !== password2) {
      setError('Las contraseñas no coinciden.');
      return;
    }

    try {
      const userData = { username, email, password, role: 'guest' }; 
      await register(userData);
      alert('¡Registro exitoso! Ahora puedes iniciar sesión.');
      navigate('/login'); 
    } catch (err) {
    
      console.error('Error en el registro:', err.response.data);
      
      const errorData = err.response.data;
      const errorMessages = Object.values(errorData).flat().join(' ');
      setError(errorMessages || 'Ocurrió un error en el registro.');
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '150px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Crear una Cuenta</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="username">Usuario</label>
          <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required style={{ width: '100%', padding: '8px', marginTop: '5px' }} />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="email">Email</label>
          <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required style={{ width: '100%', padding: '8px', marginTop: '5px' }} />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="password">Contraseña</label>
          <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required style={{ width: '100%', padding: '8px', marginTop: '5px' }} />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="password2">Confirmar Contraseña</label>
          <input type="password" id="password2" value={password2} onChange={(e) => setPassword2(e.target.value)} required style={{ width: '100%', padding: '8px', marginTop: '5px' }} />
        </div>

        {error && <p style={{ color: 'red' }}>{error}</p>}
        
        <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '4px' }}>
          Registrarse
        </button>
      </form>
      <p style={{ textAlign: 'center', marginTop: '15px' }}>
        ¿Ya tienes una cuenta? <Link to="/login">Inicia sesión aquí</Link>
      </p>
    </div>
  );
}