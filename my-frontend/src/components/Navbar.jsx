// src/components/Navbar.jsx

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Navbar.css';

import logoIcon from '../assets/logo.png';
import avatarIcon from '../assets/avatar.png'; 

export default function Navbar({ searchValue, onSearch }) {
  const navigate = useNavigate();
  const { isAuthenticated, logoutContext } = useAuth();

  const handleLogout = () => {
    logoutContext();
    navigate('/');
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo + nombre */}
        <Link to="/" className="navbar-logo">
          <img src={logoIcon} alt="Athletica Logo" className="logo-icon" />
          <span className="logo-text">Athletica</span>
        </Link>
        
        {/* ======================================= */}
        {/* =========   NUEVO ENLACE AÑADIDO    ========= */}
        {/* ======================================= */}
        <Link to="/athletes" className="navbar-link">
          Atletas
        </Link>

        {/* Buscador (se mantiene a la derecha) */}
        <div className="navbar-search">
          <input
            type="text"
            placeholder="Buscar atleta..."
            value={searchValue}
            onChange={e => onSearch(e.target.value)}
          />
          <button onClick={() => onSearch(searchValue)}>🔍</button>
        </div>

        {/* Acciones de usuario dinámicas */}
        <div className="navbar-actions">
          {isAuthenticated ? (
            // Si el usuario está autenticado
            <>
              <Link to="/profile">
                <img src={avatarIcon} alt="Perfil" className="avatar-icon" />
              </Link>
              <button onClick={handleLogout} className="logout-button">
                Cerrar Sesión
              </button>
            </>
          ) : (
            // Si el usuario no está autenticado
            <Link to="/login" className="login-button-link">
              <button className="login-button">Iniciar Sesión</button>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
}