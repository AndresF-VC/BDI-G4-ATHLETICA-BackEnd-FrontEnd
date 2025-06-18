// src/components/LoginPage.jsx

import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext'; // <-- 1. IMPORTA useAuth

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { loginContext } = useAuth(); // <-- 2. OBTÉN LA FUNCIÓN DEL CONTEXTO
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await loginContext(username, password); // <-- 3. USA LA FUNCIÓN DEL CONTEXTO
      // La alerta de éxito la podemos quitar, la redirección es suficiente
      navigate('/'); // Redirige al home después del login
    } catch (error) {
      console.error('Error en el inicio de sesión:', error);
      alert('Usuario o contraseña incorrectos.');
    }
  };

  // ... (el return con el JSX del formulario no cambia)
  return (
    <div style={{ maxWidth: '400px', margin: '150px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit}>
        {/* ... Inputs ... */}
        <div style={{ marginBottom: '15px' }}>
            <label htmlFor="username">Usuario</label><input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required style={{ width: '100%', padding: '8px', marginTop: '5px' }}/>
        </div>
        <div style={{ marginBottom: '15px' }}>
            <label htmlFor="password">Contraseña</label><input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required style={{ width: '100%', padding: '8px', marginTop: '5px' }}/>
        </div>
        <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px' }}>Entrar</button>
      </form>
      <p style={{ textAlign: 'center', marginTop: '15px' }}>
        ¿No tienes una cuenta? <Link to="/register" style={{ color: '#007bff', textDecoration: 'none' }}>Regístrate aquí</Link>
      </p>
    </div>
  );
}